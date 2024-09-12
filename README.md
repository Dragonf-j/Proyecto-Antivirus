# GestionDescargas
 Sistema para comprobar que los ficheros descagados no contengan virus. Si estos tienen virus, se procede  eliminanse de forma automatica.

 Para poder hacer uso de esta aplicacion previamente se debe indicar una seria de parametros en un fichero de configuracion de tipo JSON. Este fichero debe contener la siguiente informacion

 

 El funcionamiento para analizar se basa en el uso de la api gratuita de VirusTotal que puede analizar ficheros de hasta 32MB de tamaño. Para ficheros ficheros de mayor tamaño se usa un sistema autohospeado en un entorno local con un sistema operativo basado en Linux. El sistema usa la aplicación Cuckoo sandbox para analizar los ficheros de mayor tamaño.

 En caso de que el analisis de los ficheros indique que los ficheros no contienen virus, se procedera a mover a la ruta indicada en el fichero de configuracion.
 
 
