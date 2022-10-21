# ARCHIVO DE CONFIGURACIÓN
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

# Colección de alfabetos
# Los caracteres admitidos, así como la complejidad de los mensajes, variará según el alfabeto elegido
SIMPLE = '0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
COMPLEX = '0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚÜáéíóúü!"#$%&/()=?\'¿¡´¨+*-_,;.:[]<>|°¬\\}{ ~^`'

# Alfabeto base para cifrar/descifrar y generar las llaves de cifrado
ALPHABET = SIMPLE
# Directorio de llaves de cifrado
KEYS_DIR = 'llaves'
# Puerto de escucha por defecto
DEFAULT_PORT = 8000
# Mostrar mensajes encriptados en pantalla
SHOW_ENCRYPTED_MESSAGES = True
