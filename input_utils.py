# UTILIDADES DE ENTRADA Y SALIDA DE DATOS
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

# Importación de biblioteca de tiempo
from time import sleep
from properties import DEFAULT_PORT

# Método para seleccionar una opción
# No retorna un valor hasta que se elija una opción válida
# Las posibles opciones pueden ingresarse en forma de rango o arreglo
def select_option(message, options):
    message += '\n'
    option = input(message)
    while (not option.isdigit() or not int(option) in options):
        warning('Opción inválida')
        option = input(message)
    return int(option)

# Método para confirmar una opción
# No retorna un valor hasta que se ingrese S o N (Sí/No), sin importar mayúsculas o minúsculas
def confirm_option(message):
    message += ' [S/N]\n'
    option = input(message).upper()
    while (not option in ['S', 'N']):
        warning('Opción inválida')
        option = input(message).upper()
    return option == 'S'

# Método para leer números enteros
# No retorna un valor hasta que la entrada sea un número entero
def readInt(message):
    while (True):
        try:
            int_value = int(input(message))
            break
        except:
            warning('Entrada inválida')
    return int_value

# Método para leer direcciones ip o nombres de dominio
# Agrega un puerto por defecto en caso de no especificarse
def readAddress(message):
    address = input(message)
    if address.find(':') == -1:
        address += ':' + str(DEFAULT_PORT)
    return address

# Métodos para imprimir alertas y advertencias
# El programa se pausa un segundo para asegurar que el usuario pueda ver el mensaje
def alert(message):
    print('\n-- ' + message + ' --')
    sleep(1)

def warning(message):
    print('\n[!] ' + message + ' [!]')
    sleep(1)

# Método para limpiear texto escrito en pantalla
def clear(inline = False):
    print('\r' if inline else '\033[1A', end='\x1b[2K')

# Método para mostrar un mensaje de carga
def loading(message):
    print('\n' + message + '...')
    sleep(1)

# Método para mostrar mensaje tras mensaje de carga
def loaded(message):
    clear()
    print(message)
    sleep(1)
