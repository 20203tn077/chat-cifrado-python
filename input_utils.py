# UTILIDADES DE ENTRADA Y SALIDA DE DATOS
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 10/10/2022

# Importación de biblioteca de tiempo
from time import sleep

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
            int_message = int(input(message))
            break
        except:
            warning('Entrada inválida')
    return int_message

# Métodos para imprimir alertas y advertencias
# El programa se pausa un segundo para asegurar que el usuario pueda ver el mensaje
def alert(message):
    print('\n-- ' + message + ' --')
    sleep(1)

def warning(message):
    print('\n[!] ' + message + ' [!]')
    sleep(1)
