import logging
import requests
import time

class antiVirus:

    def scanVirusTotal(files, api):
        url = "https://www.virustotal.com/api/v3/files"
        
        #response = requests.get(url, headers=headers)
        with open(files, "rb") as file_to_scan:
            file = {"file": file_to_scan}
            response = requests.post(url, headers={"x-apikey": api}, files=file)
            if response.status_code == 200:
                #move.move.fileMove(files, destino)
                print(response.status_code)
                logging.info(f'Todo ha salido bien. Codigo: '+ str(response.status_code)+' Resultado del analisis'+response.text)
                #antiVirus.ResultAnalysis(response, headers)
                return response
            else:
                #move.move.deleteFile(files)
                logging.error(f'ha ocurrido un fallo. Codigo: '+ str(response.status_code))
                print(response.status_code)


    def ResultAnalysis(files, api):
        headers = {
            "accept": "application/json",
            "x-apikey": api,
            "content-type": "multipart/form-data"
        }
        response = antiVirus.scanVirusTotal(files, api)
        id = response.json().get("data", {}).get("id")
        url_analysis = f"https://www.virustotal.com/api/v3/analyses/"+id
        while True:
            analysis_response = requests.get(url_analysis, headers=headers)
            analysis_status = analysis_response.json().get("data", {}).get("attributes", {}).get("status")
            
            if analysis_status == "completed":
                print("Análisis completado.")
                break
            elif analysis_status == "queued":
                print("Análisis en cola, esperando...")
                time.sleep(10)  
            else:
                print(f"Estado del análisis: {analysis_status}")
                break
        url_analysis = analysis_response.json()#analysis_response.json().get("data",{"stats"}).get("malicious")
        return url_analysis
        #malicius = url_analysis["data"]["attributes"]["stats"]["malicious"]

        #suspicious = url_analysis["data"]["attributes"]["stats"]["suspicious"]
        #logging.info("Resultados del análisis. Datos maliciosos: "+str(malicius)+" Datos sospechosos: "+str(suspicious))
        #if malicius == 0 and suspicious == 0:
        #   move.move.fileMove(files, destino)
        #else:
        #   move.move.deleteFile(files)