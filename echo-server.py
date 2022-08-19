import socket
from rich.console import Console

console = Console()

'''
 Server API:

 - socket
 - bind
 - listen
 - accept
 - Client: should connect
 - write
 - read

'''

# Setting up the host as localhost and port

HOST, PORT = "127.0.0.1", 61000 

addr = (HOST, PORT)

# Note: SOCK_STREAM is for TCP/IP and SOCK_DGRAM can be used for UDP/IP (daatagrams)

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)

server.bind(addr)
server.listen(0)

# This is just so python prints with colours and time staps
console.log("[bold yellow]Server: [/bold yellow]" + "Waiting for conncetion", style="red")

connection, c_addr = server.accept()

console.log("[bold yellow]Server: [/bold yellow]" +  "Connection established with: ", c_addr, style="green")

data = connection.recv(1000)

d_data = data.decode()

console.log("[bold yellow]Server: [/bold yellow]" + "Recieved - ", d_data, style="blue")

connection.sendall(data)

console.log("[bold yellow]Server: [/bold yellow]" + "Sending  - ", d_data, style="red")

connection.close()
server.close()