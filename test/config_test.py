from config.config import BasicConfig 

BasicConfig = BasicConfig.read_json()
assert BasicConfig["ruta_origen"]
assert BasicConfig["ruta_destino"] 
assert BasicConfig["api_key"]