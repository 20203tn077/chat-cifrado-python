# ARCHIVO PRINCIPAL
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 17/10/2022

import socket
from encryption_utils import *
from file_utils import *
from input_utils import *
from connection_utils import Connection
from properties import DEFAULT_PORT, SHOW_ENCRYPTED_MESSAGES

encryption_key = generateKey()
listening_port = DEFAULT_PORT
username = socket.gethostname()
remote_username = ''

want_exit = False

# Menú principal
# Se sigue mostrando hasta que se elija la opción de salir
while not want_exit:
    print('\n====================================')
    print('>>    CHAT CIFRADO CON PYTHON     <<')
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
    option = select_option('\nSelecciona una opción:', range(1, 8))
    if option == 1:
        print('\nINICIAR CHAT')
        connection = Connection(listening_port, username)
        try:
            address = readAddress('\nIngresa la dirección del usuario remoto:\n')
            loading('Conectando')
            if connection.connect(address):
                remote_username = connection.remote_username
                loaded('Conectado con ' + remote_username)
                print('\nEspera tu turno para enviar un mensaje, escribe /salir para salir del chat')
                if (connection.first):
                    print('\nEnvía el primer mensaje')
                    
                    message = input('\n> ')
                    # Validación de salida del chat
                    if message == '/salir':
                        connection.send('/salir')
                        break
                    encrypted_message = encrypt(message, encryption_key)
                    connection.send(encrypted_message)
                    clear()
                    print('[' + username + ']: ' + message)
                    if SHOW_ENCRYPTED_MESSAGES:
                        print(' 🔒↓↓↓')
                        print('[' + username + ']: ' + encrypted_message)
                while True:
                    print('\nEsperando mensaje...', end='')
                    message = connection.listen()
                    # Validación de salida del chat
                    if message == '/salir':
                        clear(inline=True)
                        print(remote_username + ' ha abandonado el chat')
                        break
                    decrypted_message = decrypt(message, encryption_key)
                    clear(inline=True)
                    if SHOW_ENCRYPTED_MESSAGES:
                        print('[' + remote_username + ']: ' + message)
                        print(' 🔓↓↓↓')
                    print('[' + remote_username + ']: ' + decrypted_message)

                    message = input('\n> ')
                    # Validación de salida del chat
                    if message == '/salir':
                        connection.send('/salir')
                        break
                    encrypted_message = encrypt(message, encryption_key)
                    connection.send(encrypted_message)
                    clear()
                    print('[' + username + ']: ' + message)
                    if SHOW_ENCRYPTED_MESSAGES:
                        print(' 🔒↓↓↓')
                        print('[' + username + ']: ' + encrypted_message)
                        
                connection.close()
                alert('Chat finalizado')
            else:
                warning('Error al establecer conexión')
        except:
            connection.close()
            alert('Chat finalizado')
    elif option == 2:
        print('\nCAMBIAR NOMBRE DE USUARIO')
        if (confirm_option('\n¿Deseas cambiar tu nombre de usuario? se sobreescribirá el nombre actual (' + username + ')')):
            username = input('\nIngresa el nuevo nombre de usuario:\n')
            alert('Nombre cambiado')
        else:
            alert('Acción cancelada')
    elif option == 3:
        print('\nCAMBIAR PUERTO DE ESCUCHA')
        if (confirm_option('\n¿Deseas cambiar puerto de escucha? se sobreescribirá el puerto actual (' + str(listening_port) + ')')):
            listening_port = readInt('\nIngresa el nuevo número de puerto:\n')
            alert('Puerto cambiado')
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
