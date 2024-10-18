import os
import logging
from Antivirus import Sistema_Antivirus
from Move import move
from config import config

class Selectect:

    #clase encarga de usar un sistema de antivirus u otro dependiendo del tamaño del fichero
    def classify(json, ficheros):

        #declaracion de variables
        fichero = ficheros
        key = config.basicConfig.getAPIKey(json)
        carpeta_destino = config.basicConfig.getDestine(json)
        cape = config.basicConfig.getUrlCAPEv2(json)
        infoFich = os.stat(fichero)
        tamaño = infoFich.st_size
        tamañoGb = tamaño /(1024 * 1024 )

        logging.info(f"El tamaño del fichero"+fichero+" es de "+str(tamañoGb))
        #if para la comprobacion del tamaño de los ficheros. Si es menor a 32 mB se usara la api de virus total
        if tamañoGb < 32:
            url_analysis =  Sistema_Antivirus.antiVirus.ResultAnalysis(fichero, key)
            malicius = url_analysis["data"]["attributes"]["stats"]["malicious"]
            suspicious = url_analysis["data"]["attributes"]["stats"]["suspicious"]
            logging.info("Resultados del análisis. Datos maliciosos: "+str(malicius)+" Datos sospechosos: "+str(suspicious))
            #if que se encarga de enviar los ficheros a la carpeta de destino si malicio y sospcheso estan a 0, si no es el caso se eliminan
            if malicius == 0 and suspicious == 0:
                move.move.fileMove(fichero, carpeta_destino)
            else:
                move.move.deleteFile(fichero)
        else:
            Sistema_Antivirus.ALternaitivaAntivirus.alternative(fichero, cape)