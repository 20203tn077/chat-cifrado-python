# ARCHIVO PRINCIPAL
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 17/10/2022

from encryption_utils import *
from file_utils import *
from input_utils import *
from connection_utils import Connection

encryption_key = generateKey()
listening_port = 8000
username = 'Host'
guestname = ''

want_exit = False

# Menú principal
# Se sigue mostrando hasta que se elija la opción de salir
while not want_exit:
    print('\n====================================')
    print('>>           CRYPTO-CHAT          <<')
    print('====================================')
    print('Usuario: [' + username + ']')
    print('Puerto de escucha: [' + str(listening_port) + ']')
    print('Llave de cifrado: [' + encryption_key.replace('\n', '')[:13] + '...]')
    print('\nOpciones:')
    print('1.- Iniciar chat')
    print('2.- Cambiar nombre de usuario')
    print('3.- Cambiar puerto de escucha')
    print('4.- Generar llave de cifrado')
    print('5.- Importar llave de cifrado')
    print('6.- Exportar llave de cifrado')
    print('7.- Salir')
    option = select_option('\nSelecciona una opción:', range(1, 7))
    if option == 1:
        print('\n INICIAR CHAT')
        connection = Connection(listening_port)
        address = input('\nIngresa la dirección de PENDIENTE:\n')
        alert('Conectando...')
        if (connection.connect(address)):
            alert('Conectado')
            if (connection.first):
                connection.send(input('\nIngresa un mensaje:\n'))
            while True:
                print(connection.listen())
                connection.send(input('\nIngresa un mensaje:\n'))
        else:
            warning('Error al establecer conexión')
    elif option == 2:
        print('\nCAMBIAR NOMBRE DE USUARIO')
        if (confirm_option('\n¿Deseas cambiar puerto de usuario? se sobreescribirá el nombre actual (' + listening_port + ')')):
            listening_port = readInt('\nIngresa el nuevo número de puerto:\n')
            alert('Puerto cambiado')
        else:
            alert('Acción cancelada')
    elif option == 3:
        print('\nCAMBIAR PUERTO DE ESCUCHA')
        if (confirm_option('\n¿Deseas cambiar puerto de escucha? se sobreescribirá el puerto actual (' + username + ')')):
            username = readInt('\nIngresa el nuevo nombre de usuario:\n')
            alert('Nombre cambiado')
        else:
            alert('Acción cancelada')
    elif option == 4:
        print('\nGENERAR LLAVE DE CIFRADO')
        if (confirm_option('\n¿Deseas generar una nueva llave de cifrado?, esta reemplazará a la llave actual')):
            # Generación de nueva llave de cifrado
            encryption_key = generateKey()
            alert('Llave de cifrado generada')
        else:
            alert('Acción cancelada')
    elif option == 5:
        print('\nIMPORTAR LLAVE DE CIFRADO')
        if (confirm_option('\n¿Deseas importar una llave de cifrado?, esta reemplazará a la llave actual')):
            # Importación de llave de cifrado desde archivo
            # Se evalúa antes de reemplazar la clave en caso de que haya fallado la lectura del archivo
            key = get_encryption_key(input('\nIngresa el nombre del archivo:\n'))
            if key:
                encryption_key = key
                alert('Llave de cifrado importada')
            else:
                warning('No se pudo obtener la llave de cifrado')
        else:
            alert('Acción cancelada')
    elif option == 6:
        print('\nEXPORTAR LLAVE DE CIFRADO')
        # Guardado de llave de cifrado en archivo KEY
        filename = input('\nIngresa el nombre del archivo a guardar\n')
        if (save_encryption_key(filename, encryption_key)):
            alert('Llave de cifrado guardada en archivo ' + filename + '.key')
        else:
            warning('No se pudo guardar el archivo')
        print()
    elif option == 7:
        print('\nSALIR')
        if (confirm_option('\n¿Deseas salir del sistema?')):
            want_exit = True
            print('\nBye :)')
        else:
            alert('Acción cancelada')
