# -*- coding: utf-8 -*-
"""
Script para transformar las filas de un archivo (CSV, XLS, XLSX) en columnas.
"""
import pandas as pd
import sys
import os

def transformar_archivo(input_file_path):
    """
    Lee un archivo (CSV o Excel), transpone sus datos (filas a columnas)
    y guarda el resultado en un nuevo archivo CSV.
    """
    # --- ¿existe el archivo? ---
    if not os.path.exists(input_file_path):
        print(f"Error: El archivo de origen '{input_file_path}' no fue encontrado.")
        return # Termina la ejecución de la función

    # --- nombre del archivo de salida ---
    # Extrae solo el nombre del archivo de la ruta completa
    nombre_base_origen = os.path.basename(input_file_path)
    # Crea el nombre del archivo resultante
    output_file_name = f"{nombre_base_origen}_listo.csv"
    
    # leer el archivo según su extensión ---
    try:
        # os.path.splitext divide la ruta en (nombre, .extension)
        _, extension = os.path.splitext(input_file_path)
        extension = extension.lower() # Convertir a minúsculas para la comparación

        print(f"Procesando el archivo: {input_file_path}")

        # Pandas para leer el archivo. header=None trata todas las filas como datos.
        if extension == '.csv':
            df = pd.read_csv(input_file_path, header=None, sep=None, engine='python')
        elif extension in ['.xls', '.xlsx']:
            df = pd.read_excel(input_file_path, header=None)
        else:
            print(f"Error: Formato de archivo '{extension}' no soportado. Use CSV, XLS o XLSX.")
            return

    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return

    # --- Transposición ---
    # El atributo .T de un DataFrame realiza la transposición.
    print("Transformando los datos (convirtiendo filas a columnas)...")
    df_transformado = df.T

    # --- Guardar el resultado en un nuevo archivo CSV ---
    try:
        # Guardamos el DataFrame transformado.
        # index=False y header=False evitan que pandas escriba sus propios índices y cabeceras.
        df_transformado.to_csv(output_file_name, index=False, header=False)
        print("-" * 30)
        print(f"¡Éxito! Archivo transformado guardado como: {output_file_name}")
        print("-" * 30)

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo de salida: {e}")

# --- Punto de entrada principal del script ---
if __name__ == "__main__":
    # Se verifica que se haya pasado exactamente un argumento (el nombre del archivo)
    if len(sys.argv) != 2:
        print("Uso incorrecto.")
        print(f"Ejemplo: python {sys.argv[0]} nombre_de_archivo.csv")
    else:
        # El primer argumento (índice 1) es el nombre del archivo de origen
        archivo_origen = sys.argv[1]
        transformar_archivo(archivo_origen)
