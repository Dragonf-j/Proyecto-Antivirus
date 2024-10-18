import logging
import requests
import time

#clase para el uso de la api de virusTotal
class antiVirus: #Cambiar nombre de clase a Virustotal

    #funcion que se encarga de enviar los ficehros a la api para su analisis
    def scanVirusTotal(files, api):
        url = "https://www.virustotal.com/api/v3/files"
        
        with open(files, "rb") as file_to_scan:
            file = {"file": file_to_scan}
            response = requests.post(url, headers={"x-apikey": api}, files=file)
            if response.status_code == 200:
                print(response.status_code)
                logging.info(f'Todo ha salido bien. Codigo: '+ str(response.status_code)+' Resultado del analisis'+response.text)
                return response
            else:
                logging.error(f'ha ocurrido un fallo. Codigo: '+ str(response.status_code))
                print(response.status_code)

    #funcion que nos da el resultado del analiss y lo envia al fichero .log
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
        url_analysis = analysis_response.json()
        return url_analysis

#Clase para el uso de la alternativa a Visrustotal
class ALternaitivaAntivirus:
    #funcion que se encarga de enviar los ficheros al sistema alternativo para poder ser analizados
    def alternative(ruta_origen, urlCAPEv2):
        url_Cuckoo_Sandbox =urlCAPEv2
        response = requests.get(url_Cuckoo_Sandbox)
    print("Se usa la alternativa")