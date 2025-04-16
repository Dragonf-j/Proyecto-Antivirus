import os
import shutil
from pathlib import Path

# Simula el análisis de un archivo
def simular_analisis_archivo(ruta_origen):
    if "seguro" in ruta_origen.name:
        return "limpio"
    elif "infectado" in ruta_origen.name:
        return "infectado"
    return "desconocido"

# Simula el sistema de movimiento y análisis
def mover_y_analizar(origen, destino, cuarentena):
    for archivo in origen.iterdir():
        resultado = simular_analisis_archivo(archivo)
        if resultado == "limpio":
            shutil.move(str(archivo), destino / archivo.name)
        elif resultado == "infectado":
            # Aquí decides: eliminar o mandar a cuarentena
            shutil.move(str(archivo), cuarentena / archivo.name)
        else:
            pass  # ignorado

def test_movimiento_y_analisis(tmp_path):
    # Crear carpetas temporales
    carpeta_origen = tmp_path / "origen"
    carpeta_destino = tmp_path / "destino"
    carpeta_cuarentena = tmp_path / "cuarentena"
    for carpeta in [carpeta_origen, carpeta_destino, carpeta_cuarentena]:
        carpeta.mkdir()

    # Crear archivos de prueba
    archivo_seguro = carpeta_origen / "archivo_seguro.txt"
    archivo_infectado = carpeta_origen / "archivo_infectado.txt"
    archivo_seguro.write_text("contenido limpio")
    archivo_infectado.write_text("contenido sospechoso")

    # Ejecutar la simulación
    mover_y_analizar(carpeta_origen, carpeta_destino, carpeta_cuarentena)

    # Verificaciones
    assert not archivo_seguro.exists()
    assert not archivo_infectado.exists()
    assert (carpeta_destino / "archivo_seguro.txt").exists()
    assert (carpeta_cuarentena / "archivo_infectado.txt").exists()
