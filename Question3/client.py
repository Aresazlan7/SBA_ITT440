import socket
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set up the server address and port
    server_address = ('192.168.116.129', 8001)
    try:
        # Connect to the server
        client_socket.connect(server_address)
        pressure = float(input("Enter pressure in bar: "))
        client_socket.sendall(str(pressure).encode())
        atmosphere_data = client_socket.recv(1024)
        atmosphere = float(atmosphere_data.decode())
        print("Received converted atmosphere value from server: {} atm".format(atmosphere))
    except Exception as e:
        print("Error occurred:", str(e))
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
