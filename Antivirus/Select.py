import os
import logging
from Antivirus import Sistema_Antivirus
from Move import move


class Selectect:

    def classify(fichero, key, capeta_destino):
        infoFich = os.stat(fichero)
        tamaño = infoFich.st_size
        tamañoGb = tamaño /(1024 * 1024 )
        logging.info(f"El tamaño del fichero"+fichero+" es de "+str(tamañoGb))
        if tamañoGb < 32:
            url_analysis =  Sistema_Antivirus.antiVirus.ResultAnalysis(fichero, key)
            malicius = url_analysis["data"]["attributes"]["stats"]["malicious"]
            suspicious = url_analysis["data"]["attributes"]["stats"]["suspicious"]
            logging.info("Resultados del análisis. Datos maliciosos: "+str(malicius)+" Datos sospechosos: "+str(suspicious))
            if malicius == 0 and suspicious == 0:
                move.move.fileMove(fichero, capeta_destino)
            else:
                move.move.deleteFile(fichero)
        else:
            Sistema_Antivirus.ALternaitivaAntivirus