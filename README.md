
# 🛡️ GestionDescargas - Sistema de análisis automático de archivos

Este proyecto analiza archivos automáticamente según su **tamaño**, usando motores antivirus diferentes, y los **mueve o elimina** dependiendo del resultado.

---

## ✅ ¿Cómo funciona?

Según el tamaño del archivo, se usa uno de estos tres motores:

| Tamaño del archivo | Motor utilizado          |
|--------------------|--------------------------|
| < 32 MB            | 🌐 VirusTotal (API)      |
| 32–150 MB          | 🛡️ Microsoft Defender    |
| > 150 MB           | 🐚 ClamAV (en VM Windows) |

---

## 📦 Requisitos del sistema

1. **Python 3.8 o superior**
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear el archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
RUTA_ORIGEN=D:/Carpeta/Origen
RUTA_DESTINO=D:/Carpeta/Destino
APIKEY=tu_api_key_de_virustotal
LOGFILENAME=logs/app.log
```

4. Tener **ClamAV instalado** en la máquina virtual Windows  
   👉 [Descargar desde https://www.clamav.net/downloads](https://www.clamav.net/downloads)

   Asegúrate de que `clamscan.exe` o `clamdscan.exe` esté ubicado en:

```plaintext
C:\Program Files\ClamAV```

---

## 🚀 ¿Cómo se usa?

Desde la terminal, ejecuta:

```bash
python main.py
```

El sistema:

- 🔍 Analiza archivos nuevos en la carpeta origen  
- ✅ Mueve archivos **limpios** a la carpeta destino  
- 🛑 Elimina o aísla archivos **infectados**  
- 📝 Registra toda la actividad en archivos de log

---

## 📁 Estructura del proyecto

```
GestionDescargas/
├── Antivirus/
│   └── Sistema_Antivirus.py     # Análisis por tamaño
├── Move/
│   └── move.py                  # Movimiento y eliminación de archivos
├── config/
│   └── config.py                # Carga de configuración desde .env
├── main.py                      # Archivo principal
├── requirements.txt             # Dependencias del proyecto
├── .env.example                 # Plantilla de configuración
└── logs/                        # Carpeta para archivos de log
```

---

## 🧪 Test (opcional)

Puedes crear una carpeta `tests/` y usar [pytest](https://docs.pytest.org/) para verificar:

- La correcta carga del `.env`
- La validez de la API Key de VirusTotal
- El funcionamiento del movimiento de archivos

---

## ✨ Autor

Este sistema fue desarrollado como solución automatizada para entornos Windows en máquinas virtuales, con soporte multianálisis según el tamaño de los archivos.
