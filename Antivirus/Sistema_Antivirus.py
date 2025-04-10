import logging
import requests
import time

# Clase para el uso de la API de VirusTotal
class VirusTotal:

    # Función que se encarga de enviar los ficheros a la API para su análisis
    @staticmethod
    def scan_virus_total(files, api):
        url = "https://www.virustotal.com/api/v3/files"
        
        try:
            with open(files, "rb") as file_to_scan:
                file = {"file": file_to_scan}
                response = requests.post(url, headers={"x-apikey": api}, files=file)
                if response.status_code == 200:
                    logging.info(f'Todo ha salido bien. Código: {response.status_code}. Resultado del análisis: {response.text}')
                    return response
                else:
                    logging.error(f'Error al enviar el archivo. Código: {response.status_code}. Respuesta: {response.text}')
                    return None
        except Exception as e:
            logging.error(f'Error al abrir o enviar el archivo: {str(e)}')
            return None

    # Función que obtiene el resultado del análisis y lo envía al fichero .log
    @staticmethod
    def result_analysis(files, api):
        headers = {
            "accept": "application/json",
            "x-apikey": api,
            "content-type": "multipart/form-data"
        }
        response = VirusTotal.scan_virus_total(files, api)
        if not response:
            logging.error("No se pudo obtener una respuesta válida de la API.")
            return None

        # Obtener el ID del análisis
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

# Clase para el uso de la alternativa a VirusTotal
class AlternativaAntivirus:

    # Función que se encarga de enviar los ficheros al sistema alternativo para ser analizados
    @staticmethod
    def alternative(ruta_origen, url_cape_v2):
        try:
            response = requests.get(url_cape_v2)
            if response.status_code == 200:
                logging.info("El análisis con la alternativa se realizó correctamente.")
            else:
                logging.error(f"Error al usar la alternativa. Código: {response.status_code}. Respuesta: {response.text}")
        except Exception as e:
            logging.error(f"Error al conectar con la alternativa: {str(e)}")