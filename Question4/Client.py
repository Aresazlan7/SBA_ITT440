import socket
def main():
    host = '192.168.116.129'
    port = 8888
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        verse = client_socket.recv(1024).decode('utf-8')
        print("Received AlQuran Verse of the day: ")
        print(verse)
    except Exception as e:
        print("Error occurred:", str(e))
    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    main()
