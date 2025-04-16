from Move import move
from config.config import BasicConfig as basicConfig
import logging

# Configuración básica del logging
# Logging configurado por BasicConfig

def main():
    """
    Fichero principal que ejecuta el resto de módulos.
    Carga la información desde un archivo JSON y la envía al método encargado
    de la lógica de movimiento de ficheros después del análisis.
    """
    try:
          # Leer configuración desde .env
        config = basicConfig.read_env()
        basicConfig.configurar_logging(config['logFileName'])
        
        
        logging.info("Iniciando el proceso de movimiento de ficheros.")
        print("Se procede a mover los ficheros de la carpeta origen a la carpeta destino")
        

      
        
        # Configurar logging con el archivo especificado en la configuración
        if not config:
            logging.error("No se pudo cargar la configuración desde el archivo JSON.")
            return
        
        basicConfig.configurar_logging(config['logFileName'])
        move.Move.read_dir(config)
        # Ejecutar la lógica de movimiento de ficheros
      
        logging.info("Proceso completado con éxito.")
    except Exception as e:
        logging.error(f"Se produjo un error durante la ejecución: {str(e)}")

if __name__ == "__main__":
    main()

