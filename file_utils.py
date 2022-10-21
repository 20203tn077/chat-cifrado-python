# UTILIDADES DEL SISTEMA DE FICHEROS
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

# Importación de biblioteca de sistema operativo para las rutas
import os
# Importación de directorios desde archivo de configuración
from properties import KEYS_DIR

# Todos los métodos se encargan de gestionar las posibles excepciones
# Se utiliza os.path.join para generar la ruta final adecuada según el sistema operativo
# Se utiliza el parámetro encoding para que los archivos con carácteres especiales sean escritos y leidos de forma correcta
# Por seguridad, los archivos se guardan en carpetas aisladas, separandolas por tipo de archivo

# Obtener llave de cifrado desde archivo  
def get_encryption_key(name):
    try:
        file = open(os.path.join(KEYS_DIR, name + '.key'), encoding='utf-8')
        return file.read()
    except:
        return

# Guardar llave de cifrado en archivo
def save_encryption_key(name, key):
    try:
        file = open(os.path.join(KEYS_DIR, name + '.key'), 'w', encoding='utf-8')
        file.write(key)
        file.close
        return True
    except:
        return False
