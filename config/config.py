from dotenv import load_dotenv
import os
import logging

class BasicConfig:
    @staticmethod
    def read_env():
        load_dotenv()

        config = {
            "ruta_origen": os.getenv("RUTA_ORIGEN"),
            "ruta_destino": os.getenv("RUTA_DESTINO"),
            "apikey": os.getenv("APIKEY"),
            "logFileName": os.getenv("LOGFILENAME")
        }

        for key, value in config.items():
            if not value:
                raise ValueError(f"Falta la variable '{{key}}' en el archivo .env")

        return config

    @staticmethod
    def configurar_logging(ruta_log):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(ruta_log, mode='a', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )