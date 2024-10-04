# GestionDescargas
 Sistema para comprobar que los ficheros descagados no contengan virus. Si estos tienen virus, se procede  eliminanse de forma automatica.

 Para poder hacer uso de esta aplicacion previamente se debe indicar una serie de parametros en un fichero de configuracion de tipo JSON. Este fichero debe contener la siguiente informacion

- Ruta de la carpeta donde se encuentran los ficheros que se desea analizar
- Ruta de la carpeta donde se desean mover los ficheros analizados
- API Key de VirusTotal (Esta se debe optener en la web de la documentacion de la API y tiene que ser unica e intransferible)
- Ruta de los ficheros de configuracion

 El funcionamiento para analizar se basa en el uso de la api gratuita de VirusTotal que puede analizar ficheros de hasta 32MB de tamaño. Para ficheros ficheros de mayor tamaño se usa un sistema autohospeado en un entorno local con un sistema operativo basado en Linux. El sistema usa la aplicación CAPE sandbox para analizar los ficheros de mayor tamaño.

 En caso de que el analisis de los ficheros indique que los ficheros no contienen virus, se procedera a mover a la ruta indicada en el fichero de configuracion. Si durante el analisis sale que algun fichero puede contener virus o algun software malicioso este se procedera a eliminarse de forma automatica
 
 
