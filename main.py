from Move import move
from config import config
import logging

# Configuración básica del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Fichero principal que ejecuta el resto de módulos.
    Carga la información desde un archivo JSON y la envía al método encargado
    de la lógica de movimiento de ficheros después del análisis.
    """
    try:
        logging.info("Iniciando el proceso de movimiento de ficheros.")
        print("Se procede a mover los ficheros de la carpeta origen a la carpeta destino")

        # Leer configuración desde el archivo JSON
        json_config = config.basicConfig.readJson()
        if not json_config:
            logging.error("No se pudo cargar la configuración desde el archivo JSON.")
            return

        # Ejecutar la lógica de movimiento de ficheros
        move.move.readDir(json_config)
        logging.info("Proceso completado con éxito.")
    except Exception as e:
        logging.error(f"Se produjo un error durante la ejecución: {str(e)}")

if __name__ == "__main__":
    main()

