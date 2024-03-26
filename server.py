import socket


def server_program():
    host = socket.gethostname()
    port = 5000 

    server_socket = socket.socket()  
    server_socket.bind((host, port))  
    server_socket.listen(10)
    conn, address = server_socket.accept() 
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        conn.send(data.encode()) 

    conn.close() 

if _name_ == '_main_':
    server_program()