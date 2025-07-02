#!/usr/bin/env python3
"""
Script: verificar_instalar_ejemplo_lib.py

Descripción:
    Verifica si el paquete 'example_lib' está instalado en el entorno actual.
    Si no está instalado, lo instala automáticamente utilizando pip.

Uso:
    python verificar_instalar_ejemplo_lib.py
"""
import importlib
import subprocess
import sys


def instalar_si_falta(paquete: str):
    """Intenta importar un paquete y lo instala con pip si no existe."""
    try:
        importlib.import_module(paquete)
        print(f"✅ El paquete '{paquete}' ya está instalado.")
    except ImportError:
        print(f"⚠️  El paquete '{paquete}' no está instalado. Instalando…")
        subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
        print(f"✅ Instalación completada de '{paquete}'.")


if __name__ == "__main__":
    instalar_si_falta("example_lib")
