import logging
import requests
import time
import subprocess

# Clase para el uso de la API de VirusTotal
class VirusTotal:

    @staticmethod
    def scan_virus_total(files, api):
        """
        Envía un archivo a la API de VirusTotal para su análisis.
        """
        url = "https://www.virustotal.com/api/v3/files"
        try:
            with open(files, "rb") as file_to_scan:
                file = {"file": file_to_scan}
                response = requests.post(url, headers={"x-apikey": api}, files=file)
                if response.status_code == 200:
                    logging.info(f"Análisis enviado correctamente. Código: {response.status_code}.")
                    return response
                else:
                    logging.error(f"Error al enviar el archivo. Código: {response.status_code}. Respuesta: {response.text}")
                    return None
        except Exception as e:
            logging.error(f"Error al abrir o enviar el archivo: {str(e)}")
            return None

    @staticmethod
    def result_analysis(files, api):
        """
        Obtiene el resultado del análisis de VirusTotal.
        """
        headers = {
            "accept": "application/json",
            "x-apikey": api
        }
        response = VirusTotal.scan_virus_total(files, api)
        if not response:
            logging.error("No se pudo obtener una respuesta válida de la API.")
            return None

        try:
            analysis_id = response.json().get("data", {}).get("id")
            if not analysis_id:
                logging.error("No se pudo obtener el ID del análisis.")
                return None
        except Exception as e:
            logging.error(f"Error al procesar la respuesta de la API: {str(e)}")
            return None

        url_analysis = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        while True:
            try:
                analysis_response = requests.get(url_analysis, headers=headers)
                analysis_status = analysis_response.json().get("data", {}).get("attributes", {}).get("status")
                if analysis_status == "completed":
                    logging.info("Análisis completado.")
                    break
                elif analysis_status == "queued":
                    logging.info("Análisis en cola, esperando...")
                    time.sleep(10)
                else:
                    logging.warning(f"Estado del análisis desconocido: {analysis_status}")
                    break
            except Exception as e:
                logging.error(f"Error al obtener el estado del análisis: {str(e)}")
                break

        try:
            return analysis_response.json()
        except Exception as e:
            logging.error(f"Error al procesar la respuesta final del análisis: {str(e)}")
            return None


class AlternativaAntivirus:

    @staticmethod
    def alternative(ruta_origen):
        """
        Usa Microsoft Defender para analizar un archivo o carpeta.
        """
        try:
            comando = f'powershell "Start-MpScan -ScanPath \'{ruta_origen}\' -ScanType CustomScan"'
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            if resultado.returncode == 0:
                logging.info("✅ Escaneo completado con Microsoft Defender.")
                return resultado.stdout
            else:
                logging.error(f"⚠️ Error en el escaneo con Microsoft Defender. Código de salida: {resultado.returncode}")
                return None
        except Exception as e:
            logging.error(f"Error al ejecutar el escaneo con Microsoft Defender: {str(e)}")
            return None