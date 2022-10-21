# UTILIDADES DE CIFRADO
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

# Importación de biblioteca random para generar llaves de cifrado
import random
# Importación de alfabeto base desde archivo de configuración
from properties import ALPHABET

# Método para generar llaves de cifrado
# Se toma el alfabeto base y se revuelven los caracteres para generar la llave de cifrado
# Para mayor comodidad y facilidad de guardado, se devuelve una cadena en lugar de un arreglo
def generateKey():
    key = [*ALPHABET]
    random.shuffle(key)
    return ''.join(key)

# Métodos de cifrado y descifrado de mensajes
# El funcionamiento para ambos es el mismo pero intercambiando el alfabeto de origen y destino
# Se recorre el mensaje carácter a carácter
# Se busca el carácter en el alfabeto de origen y se reemplaza por el que se encuentre en la misma posición en el alfabeto de destino
# En caso de encontrar un caracter que no pertenezca al alfabeto de origen, se pasa al resultado sin modificaciones

def encrypt(message, key):
    result = ''
    for char in message:
        for i in range(len(ALPHABET)):
            if char == ALPHABET[i]:
                result += key[i]
                break
        else:
            result += char
    return result

def decrypt(message, key):
    result = ''
    for char in message:
        for i in range(len(ALPHABET)):
            if char == key[i]:
                result += ALPHABET[i]
                break
        else:
            result += char
    return result
