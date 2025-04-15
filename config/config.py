import json
import logging
import os

class BasicConfig:
    # Constantes para las claves requeridas en el JSON
    REQUIRED_KEYS = ['logFileName', 'carpeta_origen', 'carpeta_destino', 'api_virustotal']

    @staticmethod
    def read_json():
        """
        Lee y guarda la información del archivo JSON de configuración.
        """
        try:
            # Ruta del archivo JSON
            json_path = './json/data.json'
            if not os.path.exists(json_path):
                raise FileNotFoundError(f"El archivo JSON de configuración no se encontró en: {json_path}")

            # Cargar el archivo JSON
            with open(json_path, 'r') as file:
                json_data = json.load(file)

            # Validar que las claves necesarias existan en el JSON
            missing_keys = [key for key in BasicConfig.REQUIRED_KEYS if key not in json_data]
            if missing_keys:
                raise KeyError(f"Faltan las siguientes claves requeridas en el JSON: {', '.join(missing_keys)}")

            # Configurar el logging con el nombre del archivo especificado en el JSON
            BasicConfig.config_log(json_data['logFileName'])
            return json_data
        except FileNotFoundError as e:
            logging.error(str(e))
        except KeyError as e:
            logging.error(f"Error en el formato del JSON: {str(e)}")
        except json.JSONDecodeError as e:
            logging.error(f"Error al decodificar el archivo JSON: {str(e)}")
        except Exception as e:
            logging.error(f"Se ha producido un error leyendo el JSON: {str(e)}")
        return None

    @staticmethod
    def config_log(filename):
        """
        Configura el sistema de logging con el archivo de log especificado.
        """
        try:
            # Crear el archivo de log si no existe
            log_dir = os.path.dirname(filename)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            logging.basicConfig(
                filename=filename,
                level=logging.DEBUG,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            logging.info("Configuración de logging completada.")
        except Exception as e:
            logging.error(f"Error al configurar el logging: {str(e)}")

    @staticmethod
    def get_path_origin(json_data):
        return json_data.get('carpeta_origen', '')

    @staticmethod
    def get_destine(json_data):
        return json_data.get('carpeta_destino', '')

    @staticmethod
    def get_log_name(json_data):
        return json_data.get('logFileName', '')

    @staticmethod
    def get_api_key(json_data):
        return json_data.get('api_virustotal', '')

    @staticmethod
    def get_url_cape_v2(json_data):
        return json_data.get('api_virustotal', '')


