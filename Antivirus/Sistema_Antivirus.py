import subprocess
import os
import requests
import time
import logging

class Sistema_Antivirus:

    def __init__(self, config):
        self.api_key = config["apikey"]
        self.headers = {"x-apikey": self.api_key}
        self.vt_url = "https://www.virustotal.com/api/v3/files"

    def analizar_archivo(self, ruta_origen):
        file_size = os.path.getsize(ruta_origen)
        mb_size = round(file_size / (1024 * 1024), 2)
        logging.info(f"Tamaño del fichero '{ruta_origen}': {mb_size} MB.")

        if file_size < 32 * 1024 * 1024:
            return self._analizar_con_virustotal(ruta_origen)
        elif file_size < 150 * 1024 * 1024:
            return self._analizar_con_defender(ruta_origen)
        else:
            return self._analizar_con_clamav(ruta_origen)

    def _analizar_con_virustotal(self, ruta_origen):
        try:
            with open(ruta_origen, "rb") as f:
                response = requests.post(self.vt_url, headers=self.headers, files={"file": f})
            if response.status_code == 200:
                analysis_url = response.json()["data"]["id"]
                logging.info("Archivo enviado a VirusTotal correctamente. Esperando análisis...")
                return self._esperar_resultado_virustotal(analysis_url)
            else:
                logging.error(f"❌ Error al subir archivo a VirusTotal: {response.status_code}")
                return "error"
        except Exception as e:
            logging.error(f"❌ Excepción al usar VirusTotal: {e}")
            return "error"

    def _esperar_resultado_virustotal(self, analysis_id):
        analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        for _ in range(10):
            response = requests.get(analysis_url, headers=self.headers)
            if response.status_code == 200:
                result = response.json()
                stats = result["data"]["attributes"]["stats"]
                if stats["malicious"] > 0:
                    return "infectado"
                elif stats["undetected"] > 0:
                    return "limpio"
            time.sleep(5)
        logging.warning("⚠️ Timeout esperando análisis de VirusTotal.")
        return "desconocido"

    def _analizar_con_defender(self, ruta_origen):
        defender_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"

        if not os.path.exists(defender_path):
            logging.error("❌ No se encontró MpCmdRun.exe")
            return "error"

        try:
            process = subprocess.Popen(
                [defender_path, "-Scan", "-ScanType", "3", "-File", ruta_origen],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate()

            logging.info("🛡️ Defender STDOUT:" + stdout.strip())
            logging.info("🛡️ Defender STDERR:" + stderr.strip())
            logging.info(f"🛡️ Código de salida: {process.returncode}")

            if "no threats" in stdout.lower():
                return "limpio"
            elif "threat" in stdout.lower() or process.returncode == 2:
                return "infectado"
            elif "0x80508023" in stdout or "too large" in stdout.lower():
                return "no_escanable"
            elif process.returncode == 0:
                return "limpio"
            else:
                return "error"
        except Exception as e:
            logging.error(f"❌ Error ejecutando Defender: {e}")
            return "error"

    def _analizar_con_clamav(self, ruta_origen):
        try:
            clamscan_paths = [r"C:\Program Files\ClamAV\clamscan.exe", r"C:\Program Files\ClamAV\clamdscan.exe"]
            clamav = next((p for p in clamscan_paths if os.path.exists(p)), None)

            if not clamav:
                logging.error("❌ No se encontró ClamAV en las rutas esperadas.")
                return "error"

            result = subprocess.run([clamav, "--infected", "--no-summary", ruta_origen], capture_output=True, text=True)

            logging.info("🐚 ClamAV STDOUT:" + result.stdout.strip())
            logging.info("🐚 ClamAV STDERR:" + result.stderr.strip())
            logging.info(f"🐚 ClamAV código de salida: {result.returncode}")

            if result.returncode == 0:
                return "limpio"
            elif result.returncode == 1:
                return "infectado"
            else:
                return "error"

        except Exception as e:
            logging.error(f"❌ Error ejecutando ClamAV: {e}")
            return "error"