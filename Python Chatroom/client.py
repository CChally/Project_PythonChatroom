import threading
import socket

# Globals
server_ip = '127.0.0.1', 3444
#=======================================================================================================
def start_client():
    try:
        # Create a TCP/IP Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to server
        sock.connect(server_ip)
        print(f"Connected to the chat server ...")
    
        username = input("Username: ")
        pwd = input("Password: ")


        # Initialize and start threads for sending and recieving messages
        send = threading.Thread(target = send_messages, args = (sock,))
        recv = threading.Thread(target = recv_messages, args = (sock,))

        send.start()
        recv.start()

    # Handle any exceptions regarding the connection process
    except:
        print("Error connecting to the server! Is the server running?")
#=======================================================================================================
def send_messages(sock):
    while True:
        message = input("=>")
        try:
            sock.send(message.encode('utf-8'))
        except:
            print("Error generating/sending message to the server!")
            sock.close()
            break
#=======================================================================================================
def recv_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)

        except:
            print("\n\nServer closed...")
            print("Ending client... ")
            sock.close()
            break
#=======================================================================================================
if __name__ == '__main__':
    start_client()