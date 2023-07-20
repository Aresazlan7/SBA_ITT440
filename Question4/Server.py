import socket
import threading
import random
# List of quotes
AlQuran_verses = [
"So verily, with the hardship, there is a relief. Verily, with the hardship, there is relie- [Quran 94:5-6]",
"My mercy encompasses all things-[Quran 7:156]",
"Allah does not burden a soul beyond that it can bear-[Quran 2:286]",
"The truth is from your Lord, so do not be among the doubters-[Quran 3:60]"
]
def handle_client(client_socket):
    quote = random.choice(AlQuran_verses)
    client_socket.send(quote.encode('utf-8'))
    client_socket.close()
def main():
    host = '192.168.116.129'
    port = 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server is listening on {} on port {}".format(host, port))
    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)
#multithreading
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
