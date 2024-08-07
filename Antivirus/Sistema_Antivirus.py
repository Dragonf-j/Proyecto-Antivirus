from config import config
import logging
import requests

class antiVirus:

    def scanVirusTotal(files, api):
        url = "https://www.virustotal.com/api/v3/files/upload_url"
        headers = {
            "accept": "application/json",
            "x-apikey": api,
            "content-type": "multipart/form-data"
        }
        response = requests.post(url, headers, files)
        print(response.text)
        return response
