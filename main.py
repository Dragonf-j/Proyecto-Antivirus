from Move import move
from config import config

print("Se procede a mover los ficheros de la carpeta origen a la carpeta destino")
json = config.basicConfig.readJson()
move.move.readDir(json)

