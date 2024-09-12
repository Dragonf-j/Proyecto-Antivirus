# GestionDescargas
 Sistema para comprobar que los ficheros descagados no contengan virus. Si estos tienen virus, se procede  eliminanse de forma automatica.

 El funcionamiento para analizar se basa en el uso de la api gratuita de VirusTotal que puede analizar ficheros de hasta 32MB de tamaño. Para ficheros ficheros de mayor tamaño se usa un sistema autohospeado en un entorno local con un sistema operativo basado en Linux. El sistema usa la aplicación Cuckoo sandbox para analizar los ficheros
 
