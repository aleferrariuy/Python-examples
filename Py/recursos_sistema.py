import psutil

def mostrar_recursos():
    # Uso de CPU en porcentaje (espera 1 segundo para la medición)
    uso_cpu = psutil.cpu_percent(interval=5)
    # Uso de memoria RAM en porcentaje
    uso_ram = psutil.virtual_memory().percent
    # Uso de disco en la partición raíz
    uso_disco = psutil.disk_usage('/').percent

    print("\n                          Recursos del sistema\n+-------------------------------------------------------------------------+")
    print(f"  Uso de CPU: {uso_cpu}%")
    print(f"  Uso de RAM: {uso_ram}%")
    print(f"  Uso de espacio en disco (unidad principal): {uso_disco}%")
    print("+-------------------------------------------------------------------------+\n                                         Alejandro Ferrari - agfe HelpDesk")

if __name__ == "__main__":
    mostrar_recursos()
