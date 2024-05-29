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
            config.basicConfig.readJson()
            #with open('json/data.json', 'r') as file:
               # jsonData = json.load(file)
            carpeta_origen = config.basicConfig.carpeta_origen #jsonData['carpeta_origen']
            contenido_File = os.listdir(carpeta_origen)
            ficheros = [f for f in contenido_File]
            carpeta_destino = jsonData['carpeta_destino']
            for fic in ficheros:
                carpeta_origen = carpeta_origen + fic
                if os.listdir(carpeta_origen) == true:
                    move.fileMove(carpeta_origen, carpeta_destino)     
                    logging.info(f"Se leen los ficheros que hay en la carpeta: "+carpeta_origen+ " y contiene estos ficheros: "+contenido_File)
                else:
                    carpeta_origen = carpeta_origen
                
                logging.basicConfig(
                    filename='D:/proyectos/Antivirus/app.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato de los mensajes
                    datefmt='%Y-%m-%d %H:%M:%S'  # Formato de la fecha y hora
                )
        except Exception as exp:
            logging.error(f"Se ha producido un error leyendo el JSON " +str(exp) )

    @staticmethod    
    def fileMove(carpeta_origen, carpeta_destino):
        try:
            shutil.move(carpeta_origen, carpeta_destino)
            logging.info(f"Se mueven los ficheros de la carpeta de origen: " +carpeta_origen + " a la carpeta de destino: " +carpeta_destino+" correctamente")
        except Exception as exp:
             logging.error(f"Se ha producido un error al mover la carpeta " +str(exp ))
      



