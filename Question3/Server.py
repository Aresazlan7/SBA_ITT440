import socket

def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    try:
        atm_bar = float(data)
        atmosphere_standard = bar_to_atmosphere(atm_bar)
        client_socket.send(str(atmosphere_standard).encode('utf-8'))
        print("Pressure in bar from client:", atm_bar)
        print("Converted to atmosphere bar:", atmosphere_standard)
    except ValueError:
        error_message = "Invalid input. Please provide a valid pressure value in bar."
        client_socket.send(error_message.encode('utf-8'))
    client_socket.close()

def bar_to_atmosphere(atm_bar):
    return atm_bar * 0.986923

def main():
    host = '192.168.116.129'  
    port = 8001  

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening on {} on port {}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)
        handle_client(client_socket)

if __name__ == "__main__":
    main()
