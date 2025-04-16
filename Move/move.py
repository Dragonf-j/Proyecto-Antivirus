import shutil
import os
from config.config import BasicConfig
import logging
from Antivirus import Select

class Move:

    @staticmethod
    def read_dir(config):
        """
        Lee la carpeta de origen y envía los archivos para su análisis.
        """
        try:
          
            carpeta_origen = config["ruta_origen"]
            if not os.path.exists(carpeta_origen):
                logging.error(f"La carpeta de origen no existe: {carpeta_origen}")
                return

            ficheros = os.listdir(carpeta_origen)
            for fic in ficheros:
                ruta_fichero = os.path.join(carpeta_origen, fic)
                Select.Select.seleccion(config, ruta_fichero)

            logging.info("Se completó la lectura y clasificación de los ficheros.")
        except Exception as exp:
            logging.error(f"Se ha producido un error al leer la carpeta de origen: {str(exp)}")

    @staticmethod
    def file_move(carpeta_origen, carpeta_destino):
        """
        Mueve los archivos de la carpeta de origen a la carpeta de destino.
        """
        try:
            if not os.path.exists(carpeta_origen):
                logging.error(f"La carpeta de origen no existe: {carpeta_origen}")
                return

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
                logging.info(f"Se creó la carpeta de destino: {carpeta_destino}")

            shutil.move(carpeta_origen, carpeta_destino)
            logging.info(f"Archivos movidos de {carpeta_origen} a {carpeta_destino}.")
        except Exception as exp:
            logging.error(f"Error al mover los archivos: {str(exp)}")

    @staticmethod
    def delete_file(carpeta):
        """
        Elimina archivos o carpetas.
        """
        try:
            if not os.path.exists(carpeta):
                logging.warning(f"La carpeta o archivo a eliminar no existe: {carpeta}")
                return

            if os.path.isfile(carpeta):
                os.remove(carpeta)
                logging.info(f"Archivo eliminado: {carpeta}")
            else:
                shutil.rmtree(carpeta)
                logging.info(f"Carpeta eliminada: {carpeta}")
        except Exception as exp:
            logging.error(f"Error al eliminar los datos: {str(exp)}")




