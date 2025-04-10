import os
import logging
from Antivirus import Sistema_Antivirus
from Move import move
from config import config

class Select:

    # Clase encargada de usar un sistema de antivirus u otro dependiendo del tamaño del fichero
    @staticmethod
    def classify(json, fichero):
        try:
            # Validar que el fichero exista
            if not os.path.exists(fichero):
                logging.error(f"El fichero no existe: {fichero}")
                return

            # Declaración de variables
            key = config.basicConfig.getAPIKey(json)
            carpeta_destino = config.basicConfig.getDestine(json)
            cape = config.basicConfig.getUrlCAPEv2(json)
            info_fich = os.stat(fichero)
            tamaño = info_fich.st_size
            tamaño_mb = tamaño / (1024 * 1024)

            logging.info(f"El tamaño del fichero '{fichero}' es de {tamaño_mb:.2f} MB.")

            # Comprobación del tamaño del fichero
            if tamaño_mb < 32:
                # Usar la API de VirusTotal
                url_analysis = Sistema_Antivirus.VirusTotal.result_analysis(fichero, key)
                if not url_analysis:
                    logging.error(f"No se pudo obtener el análisis para el fichero: {fichero}")
                    return

                # Extraer resultados del análisis
                try:
                    malicious = url_analysis["data"]["attributes"]["stats"]["malicious"]
                    suspicious = url_analysis["data"]["attributes"]["stats"]["suspicious"]
                    logging.info(f"Resultados del análisis. Maliciosos: {malicious}, Sospechosos: {suspicious}")
                except KeyError as e:
                    logging.error(f"Error al extraer los resultados del análisis: {str(e)}")
                    return

                # Mover o eliminar el fichero según los resultados
                if malicious == 0 and suspicious == 0:
                    move.Move.file_move(fichero, carpeta_destino)
                else:
                    move.Move.delete_file(fichero)
            else:
                # Usar el sistema alternativo si el fichero es mayor a 32 MB
                Sistema_Antivirus.AlternativaAntivirus.alternative(fichero, cape)
        except Exception as e:
            logging.error(f"Se produjo un error al clasificar el fichero: {str(e)}")