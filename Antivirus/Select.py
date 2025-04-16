import os
from Antivirus.Sistema_Antivirus import Sistema_Antivirus

class Select:
    @staticmethod
    def seleccion(config, file_path):
        size_mb = os.path.getsize(file_path) / (1024 * 1024)
        sistema = Sistema_Antivirus(config)

        if size_mb < 32:
            return sistema._analizar_con_virustotal(file_path)
        elif 32 <= size_mb < 150:
            return sistema._analizar_con_defender(file_path)
        else:
            return sistema._analizar_con_clamav(file_path)