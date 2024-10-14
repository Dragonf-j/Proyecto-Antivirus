from Move import move
from config import config
#Fichero principal que hace que el resto de ficheros se ejecute. En este fichero tambien se carga la informacion de json en una variabel y se envia al metodo que se encarga de la logica de movimiento de ficheros luego del analisis
print("Se procede a mover los ficheros de la carpeta origen a la carpeta destino")
json = config.basicConfig.readJson()
move.move.readDir(json)

