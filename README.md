# GestionDescargas
 Sistema para comprobar que los ficheros descagados no contengan virus. En caso de que los tengan, se eliminan de forma automática.

 Para poder hacer uso de esta aplicación, previamente se deben indicar una serie de parámetros en un fichero de configuración de tipo JSON. Este fichero debe contener la siguiente información:

- Ruta de la carpeta donde se encuentran los ficheros que se desean analizar
- Ruta de la carpeta donde se desean mover los ficheros analizados
- API Key de VirusTotal (esta debe obtenerse en la web de la documentación de la API y tiene que ser única e intransferible)
- Ruta de los ficheros de configuración

 El funcionamiento se basa en el uso de la API gratuita de VirusTotal que puede analizar ficheros de hasta 32MB de tamaño. Para ficheros de mayor tamaño se usa un sistema autohospeado en un entorno local con un sistema operativo basado en Linux. Este usa la aplicación CAPE sandbox para analizar los ficheros de mayor tamaño.

 En caso de que el análisis de los ficheros indique que no contienen virus, se procederá a mover a la ruta indicada en el fichero de configuración. Si durante el análisis sale que alguún fichero puede contener virus o algún software malicioso, este se eliminará de forma automática.
 
 
