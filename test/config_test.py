from config.config import BasicConfig 

basicConfig = BasicConfig.read_env()
assert basicConfig["ruta_origen"] is not None
assert basicConfig["ruta_destino"] is not None
assert basicConfig["apikey"] is not None
assert basicConfig["logFileName"] is not None