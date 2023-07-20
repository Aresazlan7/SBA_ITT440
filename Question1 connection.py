import socket

def main():
    host = "izani.synology.me"
    port = 8443

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((host, port))

        student_id = "2021530085" 
        client_socket.sendall(student_id.encode())

        response = client_socket.recv(1024).decode()

        print("Received unique URL from the server:", response)

    except ConnectionRefusedError:
        print("Connection to the server refused. Please check the hostname and port.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        
        client_socket.close()

if __name__ == "__main__":
    main()


