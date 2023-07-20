#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <signal.h>

int client_fd;

void sigint_handler(int sig) {
    // Close the socket before exiting
    close(client_fd);
    printf("\nExiting the program.\n");
    exit(0);
}

int main() {
    signal(SIGINT, sigint_handler); // Register SIGINT signal handler

    struct sockaddr_in server_addr;

    client_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (client_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = inet_addr("192.168.116.129"); // Server IP address
    server_addr.sin_port = htons(8000);

    if (connect(client_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Connection failed");
        close(client_fd);
        exit(EXIT_FAILURE);
    }

    int received_number;
    char choice;

    do {
        send(client_fd, &choice, sizeof(choice), 0);
        recv(client_fd, &received_number, sizeof(received_number), 0);
        printf("Received random number from server: %d\n", received_number);

        printf("Do you want to continue receiving random numbers? (y/n): ");
        fflush(stdout);

        if (scanf(" %c", &choice) != 1) {
            printf("Invalid input. Exiting the program.\n");
            break;
        }
    } while (choice == 'y' || choice == 'Y');

    close(client_fd);

    return 0;
}

