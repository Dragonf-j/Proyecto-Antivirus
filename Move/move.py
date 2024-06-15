import shutil
import json
import os
from config import config
import logging

class move:
    carpeta_destino = ''
    carpeta_origen = ''
    contenido_File = ''
    @staticmethod
    def readDir():
        
        try:
            json = config.basicConfig.readJson()
            carpeta_origen = config.basicConfig.getPathOrigin(json) 
            contenido_File = os.listdir(carpeta_origen)
            ficheros = [f for f in contenido_File]
            carpeta_destino = config.basicConfig.getDestine(json)
            for fic in ficheros:
                carpeta= carpeta_origen + fic
                move.fileMove(carpeta, carpeta_destino)     
                logging.info(f"Se lee el fichero: {carpeta} y se mueve a: {carpeta_destino}")
            config.basicConfig.configLog(config.basicConfig.getLogName(json))
                
        except Exception as exp:
            logging.error(f"Se ha producido un error" +str(exp) )

    @staticmethod    
    def fileMove(carpeta_origen, carpeta_destino):
        try:
            shutil.move(carpeta_origen, carpeta_destino)
            logging.info(f"Se mueven los ficheros de la carpeta de origen: " +carpeta_origen + " a la carpeta de destino: " +carpeta_destino+" correctamente")
        except Exception as exp:
            logging.error(f"Se ha producido un error al mover la carpeta " +str(exp ))




