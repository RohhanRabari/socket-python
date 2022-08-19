import socket
from rich.console import Console

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
console = Console()

S_HOST, S_PORT = "127.0.0.1", 61000
C_HEADER = "[bold magenta]Client: [/bold magenta]"

s_addr = (S_HOST, S_PORT)

client.connect(s_addr)

message = input()

console.log(C_HEADER + "Sending - ", message, style="red")

client.sendall(message.encode())

data = client.recv(1000).decode()

console.log(C_HEADER + "[bold green]Server Echoed - [/ bold green]", data, style="green")

client.close()