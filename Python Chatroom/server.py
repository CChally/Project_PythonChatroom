import threading
import socket
from interact_db.db_handler import authenticate, register

# Globals
clients = []
address = ('0.0.0.0', 3444)
lock = threading.Lock()

#=======================================================================================================
def start_server():

    # Create server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to Socket
    server.bind(address)

    # Listen to socket
    server.listen(5)
    print(f"Server started listening to port {address[1]} ")

    # Accept Client connections
    while True:
        try:
            client_socket, client_address = server.accept()
            print(f"New connection from {client_address}")

            # Authenticate account
            username = authenticate(client_socket, client_address)

            with lock:
                clients.append(client_socket)
            client = threading.Thread(target = handle_client, args = (client_socket, client_address))
            client.start()
        except:
            print("Closing server ... ")
            server.close()
#=======================================================================================================
def handle_client(client_socket, client_address):

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            
            # Client gracefully disconnecting
            if message == '/quit':
                print(f"{client_address} gracefully disconnected")
                with lock:
                    clients.remove(client_socket)
                client_socket.close()
                break

            # Valid message, broadcast to all clients in chatroom
            broadcast(client_socket, client_address, message)

        # All other cases
        except:
            print(f"{client_address} disconnected")
            with lock:
                clients.remove(client_socket)
            client_socket.close()
            break
#=======================================================================================================
def broadcast(curr_client, client_addr, message):
    print(f"{client_addr} : {message}")
    broadcast = f"{client_addr} : {message}"
    for client in clients:
        if(client != curr_client):
            try:
                client.send(broadcast.encode('utf-8'))
            except:
                print("Error in broadcasting message to other clients!")
#=======================================================================================================
if __name__ == '__main__':
    start_server()