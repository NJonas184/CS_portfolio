import socket

hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)

print(f"name: {hostName}")
print(f"IP: {hostIP}")


server_ip = "192.168.56.1"
server_port = 9234

# Exercise : how to find if the port is in use:
# 1. Using command line in linux/windows
# 2. In python

server_addr = (server_ip, server_port) # Remember it is a tuple you dummy

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket

# SOCK_STREAM = Stream of bytes

server_socket.bind(server_addr) # Bind to address

print("Listening for clients")

server_socket.listen(5) # Listen for clients

conn, address = server_socket.accept() # Receiving tuple with (socket, address)

print("Client Accepted!")

# Exercise : Learn how to use flags
message = conn.recv(1024).decode("utf-8") # Specify size in Bytes
# Also make sure the decoding is the same as the encoding

splitMsg = message.split(" ")

if splitMsg[0] == "GET":
    print(f"Recieved a GET request from client {address[0]}")
    response = "Ok, sending the data!"
    server_socket.send(response.encode("utf-8"))

#print(message)

conn.close()

# We recieved a <command> from client <IP>


server_socket.close() # Probably will give an error
