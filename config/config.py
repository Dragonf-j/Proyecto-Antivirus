import json
import logging
import os

class BasicConfig:
    carpeta_destino = ''
    carpeta_origen = ''
    filename = ''

    @staticmethod
    def read_json():
        """
        Lee y guarda la información del archivo JSON de configuración.
        """
        try:
            with open('./json/data.json', 'r') as file:
                json_data = json.load(file)

            # Validar que las claves necesarias existan en el JSON
            required_keys = ['logFileName', 'carpeta_origen', 'carpeta_destino', 'api-VirusTotal']
            for key in required_keys:
                if key not in json_data:
                    raise KeyError(f"Falta la clave requerida en el JSON: {key}")

            filename = json_data['logFileName']
            BasicConfig.config_log(filename)
            return json_data
        except FileNotFoundError:
            logging.error("El archivo JSON de configuración no se encontró.")
        except KeyError as exp:
            logging.error(f"Error en el formato del JSON: {str(exp)}")
        except Exception as exp:
            logging.error(f"Se ha producido un error leyendo el JSON: {str(exp)}")
        return None

    @staticmethod
    def config_log(filename):
        """
        Configura el sistema de logging con el archivo de log especificado.
        """
        try:
            logging.basicConfig(
                filename=filename,
                level=logging.DEBUG,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            logging.info("Configuración de logging completada.")
        except Exception as exp:
            logging.error(f"Error al configurar el logging: {str(exp)}")

    @staticmethod
    def get_path_origin(json_data):
        """
        Obtiene la ruta donde se encuentran los ficheros originalmente.
        """
        return json_data.get('carpeta_origen', '')

    @staticmethod
    def get_destine(json_data):
        """
        Obtiene la ruta donde serán enviados los ficheros analizados.
        """
        return json_data.get('carpeta_destino', '')

    @staticmethod
    def get_log_name(json_data):
        """
        Obtiene el nombre del fichero log para llevar un registro.
        """
        return json_data.get('logFileName', '')

    @staticmethod
    def get_api_key(json_data):
        """
        Obtiene la clave de la API de VirusTotal para ser usada.
        """
        return json_data.get('api-VirusTotal', '')

    @staticmethod
    def get_url_cape_v2(json_data):
        """
        Obtiene la URL del sistema alternativo.
        """
        return json_data.get('api-VirusTotal', '')


