import shutil
import os
from config import config
import logging
from Antivirus import Select


class move:
    #clase que lee la carpeta de origen con su contenido y que se encarga de enviar los ficheros para su analisis
    def readDir(json):
        
        try:
            carpeta_origen = config.basicConfig.getPathOrigin(json) 
            contenido_File = os.listdir(carpeta_origen)
            ficheros = [f for f in contenido_File]
            for fic in ficheros:
                carpeta= carpeta_origen + fic
                Select.Selectect.classify(json, carpeta)
            config.basicConfig.configLog(config.basicConfig.getLogName(json))
                
        except Exception as exp:
            logging.error(f"Se ha producido un error" +str(exp) )

    #clase encarga de mover los ficheros no infectados de la carpeta de origen a la carpeta de destino
    def fileMove(carpeta_origen, carpeta_destino):
        try:
            shutil.move(carpeta_origen, carpeta_destino)
            logging.info(f"Se mueven los ficheros de la carpeta de origen: " +carpeta_origen + " a la carpeta de destino: " +carpeta_destino+" correctamente")
        except Exception as exp:
            logging.error(f"Se ha producido un error al mover los ficheros de la carpeta de origen " +str(exp ))

    #clase encarga de eliminar los ficehros infectados una vez que ha terminado el analisis
    def deleteFile(carpeta):
        try:
            logging.info(f"Se procede a eliminar los datos ubicados en la " +carpeta)
            if os.path.isfile == True:
                os.remove(carpeta)
            else:
                shutil.rmtree(carpeta)
        except Exception as exp:
            logging.error(f"Se ha producido un error al eliminar los datos  " +str(exp ))




