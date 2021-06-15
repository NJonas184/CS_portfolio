import socket
import time

# 1. Create a socket
# 2. Connect to a remote server
# 3. Ask user to enter message
# 4. send that message to the server
# 5. close it


hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)

client_ip = hostIP
client_port = 10001

server_ip = "192.168.56.1"
server_port = 9234

server_addr = (server_ip, server_port)

client_addr = (client_ip, client_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_addr)

message = input("Type a HTTP request for the server: ") # Header + data

splitMsg = message.split("\n\n")

command = splitMsg[0]
data = splitMsg[1]

client_socket.send(command.encode('utf-8')) # Turns message into a byte string

time.sleep(2)

client_socket.close()


# GET, POST, PUT, DELETE, HEAD

# <Command> <Memory> \n\ndata 

# GET <filename>

# Header
# blank line
#(data)


