import json
import logging

class basicConfig:
    carpeta_destino = ''
    carpeta_origen = ''
    filename = ''
    @staticmethod
    def readJson():
        
        try:
            with open('./json/data.json', 'r') as file:
                jsonData = json.load(file)
                #basicConfig.addOrigin(jsonData)
                carpeta_origen = jsonData['carpeta_origen']
                carpeta_destino = jsonData['carpeta_destino']
                filename = jsonData['logFileName']
            basicConfig.configLog(filename)              
        except Exception as exp:
            logging.error(f"Se ha producido un error leyendo el JSON " +str(exp) )
    
    def addOrigin(json):
        try:
            carpeta_origen = json['carpeta_origen']      
            return carpeta_origen  
        except Exception as exp:
            logging.error(f"Se ha producido un error leyendo el JSON " +str(exp) )
    def addDestine(json):
        try:
            carpeta_destino = json['carpeta_destino']      
            return carpeta_destino  
        except Exception as exp:
            logging.error(f"Se ha producido un error leyendo el JSON " +str(exp) )

    def configLog(filename):
        logging.basicConfig(
        filename=filename,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato de los mensajes
        datefmt='%Y-%m-%d %H:%M:%S'  # Formato de la fecha y hora
        )


