import json
from django.core.management import call_command
from django.conf import settings
import os


def load_backup():
    try:
        # Configura la codificación
        with open('data_backup.json', 'r', encoding='ISO-8859-1') as file:
            data = json.load(file)

        # Guarda con codificación UTF-8
        with open('data_backup_utf8.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        # Carga los datos
        call_command('loaddata', 'data_backup_utf8.json')

        print("Datos importados exitosamente")

    except Exception as e:
        print(f"Error al importar datos: {str(e)}")

    finally:
        # Limpia el archivo temporal
        if os.path.exists('data_backup_utf8.json'):
            os.remove('data_backup_utf8.json')


if __name__ == "__main__":
    load_backup()
