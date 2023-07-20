#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#define PORT 8000
int generate_random_number() {
    // Generate a random number between 100 and 999
    return rand() % (999 - 100 + 1) + 100;
}
int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket fail to create");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Bind the socket to  address and port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 1) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Server connecting to port %d\n", PORT);
    while (1) {
        int random_number = generate_random_number();
        printf("Generated random number: %d\n", random_number);
        // Accept a new connection
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
            perror("Accept failed");
            exit(EXIT_FAILURE);
        }
        // Send the random number to the client
        send(new_socket, &random_number, sizeof(random_number), 0);
        printf("Random number %d sent to the client.\n", random_number);
        // Close the connection with the current client
        close(new_socket); 
   }
    close(server_fd);
    return 0;
}
