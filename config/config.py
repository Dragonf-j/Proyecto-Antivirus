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
                filename = jsonData['logFileName']
                
            basicConfig.configLog(filename)
            return jsonData
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
    def getPathOrigin(jsonData):
        carpeta_origen = jsonData['carpeta_origen']
        return carpeta_origen
    def getDestine(jsonData):
        carpeta_destino = jsonData['carpeta_destino']
        return carpeta_destino
    def getLogName(jsonData):
        filename = jsonData['logFileName']
        return filename
    def getAPIKey(jsonData):
        apiKey = jsonData['api-VirusTotal']
        return apiKey


