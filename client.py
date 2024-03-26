import socket


def client_program():
    host = socket.gethostname()  
    port = 5000 

    client_socket = socket.socket() 
    client_socket.connect((host, port)) 

    message = input(" ") 

    while message.lower().strip() != '\n':
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode() 
        message = input("  ")  

    client_socket.close() 

if _name_ == '_main_':
    client_program()