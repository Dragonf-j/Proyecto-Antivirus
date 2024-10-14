import json
import logging

class basicConfig:
    carpeta_destino = ''
    carpeta_origen = ''
    filename = ''
    @staticmethod
    #funcion que lee y guarda la informacion del json de configuracion
    def readJson():
        
        try:
            with open('./json/data.json', 'r') as file:
                jsonData = json.load(file)
                filename = jsonData['logFileName']
            basicConfig.configLog(filename)
            return jsonData
        except Exception as exp:
            logging.error(f"Se ha producido un error leyendo el JSON " +str(exp) )

    #funcion de la configuracion del json
    def configLog(filename):
        logging.basicConfig(
        filename=filename,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato de los mensajes
        datefmt='%Y-%m-%d %H:%M:%S'  # Formato de la fecha y hora
        )

    #funcion que optiene la ruta donde se encuentran los ficheros originalmente
    def getPathOrigin(jsonData):
        carpeta_origen = jsonData['carpeta_origen']
        return carpeta_origen
    
    #funcion que optiene la ruta donde seran enviados los ficheros analizados
    def getDestine(jsonData):
        carpeta_destino = jsonData['carpeta_destino']
        return carpeta_destino
    
    #funcion que optiene el nombre del fichero log para poder llevar un registro
    def getLogName(jsonData):
        filename = jsonData['logFileName']
        return filename
    
    #funcion que optiene la Key de la Api de virus total para poder ser usada
    def getAPIKey(jsonData):
        apiKey = jsonData['api-VirusTotal']
        return apiKey
    
    #funcion que optiene la url del sistema alternativo
    def getUrlCAPEv2(jsonData):
        cape = jsonData['api-VirusTotal']
        return cape


