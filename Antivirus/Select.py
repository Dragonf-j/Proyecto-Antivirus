import os
import logging
from Antivirus import Sistema_Antivirus
from Move import move
from config.config import BasicConfig

class Select:

    @staticmethod
    def classify(json, fichero):
        """
        Clasifica un archivo según su tamaño y lo analiza con el sistema adecuado.
        """
        try:
            if not os.path.exists(fichero):
                logging.error(f"El fichero no existe: {fichero}")
                return

            key = BasicConfig.get_api_key(json)
            carpeta_destino = BasicConfig.get_destine(json)
            cape = BasicConfig.get_url_cape_v2(json)
            tamaño_mb = os.stat(fichero).st_size / (1024 * 1024)

            logging.info(f"Tamaño del fichero '{fichero}': {tamaño_mb:.2f} MB.")

            if tamaño_mb < 32:
                url_analysis = Sistema_Antivirus.VirusTotal.result_analysis(fichero, key)
                if not url_analysis:
                    logging.error(f"No se pudo obtener el análisis para el fichero: {fichero}")
                    return

                stats = url_analysis.get("data", {}).get("attributes", {}).get("stats", {})
                malicious = stats.get("malicious", 0)
                suspicious = stats.get("suspicious", 0)
                logging.info(f"Resultados del análisis. Maliciosos: {malicious}, Sospechosos: {suspicious}")

                if malicious == 0 and suspicious == 0:
                    move.Move.file_move(fichero, carpeta_destino)
                else:
                    move.Move.delete_file(fichero)
            else:
                Sistema_Antivirus.AlternativaAntivirus.alternative(fichero)
        except Exception as e:
            logging.error(f"Error al clasificar el fichero: {str(e)}")