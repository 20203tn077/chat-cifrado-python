# CLASE DE CONEXIÓN
# Autor: Ricardo Cárdenas Guevara
# Fecha de creación: 18/10/2022
 
import socket

class Connection:
    # Método constructor
    # Al crear el objeto, se inicializa el socket y se guarda para poder utilizarse después
    def __init__(self, port, username):
        self.listening_port = port
        self.username = username
        
    # Método para establecer conexión con otra instancia del programa
    # El programa establece de forma automática su rol en la conexión
    def connect(self, full_address):
        address, port = full_address.split(':', 1)
        port = int(port)
        
        try:
            # Intenta conexión como cliente
            connection_socket = socket.socket()
            connection_socket.connect((address, port))
            self.connection = connection_socket
            # Si llega a este punto, se considera cliente y obtiene derecho a mandar el primer mensaje

            # Intercambio de nombres de usuario
            self.connection.send(self.username.encode('UTF-8'))
            self.remote_username = self.connection.recv(1024).decode('UTF-8')
            
            self.first = True
            return True
        except:
            # Falla conexión como cliente, cambia a modo servidor
            try:
                # Obtiene la ip del dispositivo en la red en la que esté conectado
                connection_socket = socket.socket()
                connection_socket.bind( ('', self.listening_port) )
                connection_socket.listen(5)
                # Sobreescribe la conexión, y obtiene la ip del dispositivo remoto
                self.connection, self.remote_address = connection_socket.accept()
                # Si llega a este punto, se considera servidor y queda a la espera del mensaje del cliente
                
                # Intercambio de nombres de usuario
                self.remote_username = self.connection.recv(1024).decode('UTF-8')
                self.connection.send(self.username.encode('UTF-8'))

                self.first = False
                return True
            except:
                # Falla como servidor, no se logró establecer conexión
                return False
            
    # Método para enviar mensaje
    def send(self, message):
        self.connection.send(message.encode('UTF-8'))
        
    # Método para escuchar y recibir mensaje
    # Queda en modo de espera y no retorna un valor hasta que llegue algún mensaje
    def listen(self):
        data = ''
        
        while not data:
            data = self.connection.recv(1024)
            
        return data.decode('UTF-8')
        
    # Método para cerrar conexión
    def close(self):
        self.connection.close()