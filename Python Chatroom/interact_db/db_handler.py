import pymysql
import bcrypt
#=======================================================================================================
def authenticate(client_socket, client_address):

    # Connect to database with creds
    try:
        connection = pymysql.connect(
            host="localhost",
            port = 3306,
            user="root",
            password="61ef255efCHDIR1f3!",
            database="chatroom"
        )
    except:
        print("Error connecting to the database!")
        client_socket.send("SERVER: Could not authenticate!".encode('utf-8'))
        client_socket.close()

        # Obtain username & password
        user = client_socket.recv(1024).decode('utf-8')
        pwd = client_socket.recv(1024).decode('utf-8')

        # Select record
        query = f"SELECT username, password, salt, WHERE username = {user}"



        # If username and password are correct, authenticate and allow into chatroom

        # If not, then prompt to register or 

#=======================================================================================================
def obtain_credentials(client_socket):
    print("obtain")
#=======================================================================================================
def hash_password(pwd):
    print("hash")

#=======================================================================================================
def register():
    print("Register")
#=======================================================================================================

