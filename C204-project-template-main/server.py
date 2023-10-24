
import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()

     
        playerName = player_socket.recv(1024).decode().strip()

   
        if (len(CLIENTS.keys()) == 0):
            CLIENTS[playerName] = {"player_type":"player1"}
        else :
            CLIENTS[playerName] = {"player_type":"player2"}
        
        CLIENTS[playerName]["player_socket"] = player_socket
        CLIENTS[playerName]["address"] = addr
        CLIENTS[playerName]["player_name"] = playerName
        CLIENTS[playerName]["turn"] = False
        print(f"connections established with {playerName} : {addr}")





def setup():
    print("\n")
    print("\t\t\t\t\t\t*** TAMBOOLA FAMILY GAME ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup()
