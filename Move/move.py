import shutil
import os
from config import config
import logging
from Antivirus import Select


class Move:
    # Clase que lee la carpeta de origen con su contenido y se encarga de enviar los ficheros para su análisis
    @staticmethod
    def read_dir(json):
        try:
            carpeta_origen = config.basicConfig.getPathOrigin(json)
            if not os.path.exists(carpeta_origen):
                logging.error(f"La carpeta de origen no existe: {carpeta_origen}")
                return

            contenido_file = os.listdir(carpeta_origen)
            ficheros = [f for f in contenido_file]
            for fic in ficheros:
                carpeta = os.path.join(carpeta_origen, fic)
                Select.Selectect.classify(json, carpeta)

            config.basicConfig.configLog(config.basicConfig.getLogName(json))
            logging.info("Se completó la lectura y clasificación de los ficheros.")
        except Exception as exp:
            logging.error(f"Se ha producido un error al leer la carpeta de origen: {str(exp)}")

    # Clase encargada de mover los ficheros no infectados de la carpeta de origen a la carpeta de destino
    @staticmethod
    def file_move(carpeta_origen, carpeta_destino):
        try:
            if not os.path.exists(carpeta_origen):
                logging.error(f"La carpeta de origen no existe: {carpeta_origen}")
                return

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
                logging.info(f"Se creó la carpeta de destino: {carpeta_destino}")

            shutil.move(carpeta_origen, carpeta_destino)
            logging.info(f"Se movieron los ficheros de la carpeta de origen: {carpeta_origen} a la carpeta de destino: {carpeta_destino} correctamente.")
        except Exception as exp:
            logging.error(f"Se ha producido un error al mover los ficheros: {str(exp)}")

    # Clase encargada de eliminar los ficheros infectados una vez que ha terminado el análisis
    @staticmethod
    def delete_file(carpeta):
        try:
            if not os.path.exists(carpeta):
                logging.warning(f"La carpeta o archivo a eliminar no existe: {carpeta}")
                return

            logging.info(f"Se procede a eliminar los datos ubicados en: {carpeta}")
            if os.path.isfile(carpeta):
                os.remove(carpeta)
                logging.info(f"Archivo eliminado: {carpeta}")
            else:
                shutil.rmtree(carpeta)
                logging.info(f"Carpeta eliminada: {carpeta}")
        except Exception as exp:
            logging.error(f"Se ha producido un error al eliminar los datos: {str(exp)}")




