🛡️ GestionDescargas - Sistema de análisis automático de archivos
Este proyecto analiza archivos automáticamente según su tamaño y los mueve o elimina en función del resultado del análisis antivirus.

✅ ¿Cómo funciona?
Según el tamaño del archivo, se usa uno de estos tres motores:


Tamaño del archivo	Motor utilizado
< 32 MB	🌐 VirusTotal (API)
32–150 MB	🛡️ Microsoft Defender
> 150 MB	🐚 ClamAV (en Windows VM)
📦 Requisitos del sistema
1. Python 3.8+
2. Instalar dependencias:
bash
Copiar
Editar
pip install -r requirements.txt
3. Crear el archivo .env en la raíz del proyecto:
env
Copiar
Editar
RUTA_ORIGEN=D:/Carpeta/Origen
RUTA_DESTINO=D:/Carpeta/Destino
APIKEY=tu_api_key_de_virustotal
LOGFILENAME=logs/app.log
4. Tener ClamAV instalado en la máquina virtual (solo se usa para archivos grandes)
Instala desde: https://www.clamav.net/downloads

Y asegúrate de que el ejecutable clamscan.exe o clamdscan.exe esté en:

makefile
Copiar
Editar
C:\Program Files\ClamAV\
🚀 Uso
bash
Copiar
Editar
python main.py
Analiza archivos nuevos en la carpeta de origen

Mueve los archivos limpios a destino

Elimina o mueve los infectados a cuarentena

Crea un log diario de lo procesado
 
