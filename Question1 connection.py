import socket
def main():
    server_ip = "izani.synology.me"
    server_port = 8443
    student_id = input("Enter your UiTM Student ID: ")
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.send(student_id.encode())
        # Read the server response
        server_response = client_socket.recv(1024).decode()
        print("Server response:", server_response)
        # Close the connection
        client_socket.close()
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    main()


