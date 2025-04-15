import requests
from config.config import BasicConfig

def test_virustotal_api_key():
    config = BasicConfig.read_env()
    headers = {
        "x-apikey": config["apikey"]
    }

    # Probamos una solicitud con un ID inválido (pero usando nuestra API key)
    url = "https://www.virustotal.com/api/v3/files/invalid_file_id"
    response = requests.get(url, headers=headers)

    # La clave es válida si NO recibimos 401 (no autorizado)
    assert response.status_code != 401, "❌ API Key inválida o no autorizada"
    assert response.status_code in [403, 404], f"⚠️ Error inesperado: {response.status_code}"
