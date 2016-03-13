import socket

class client():
	clientsocket = None

	def __init__(self, port=None):
		self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect(port)
		self.send()
		return self.clientsocket

	def connect(self, port):
		self.clientsocket.connect(('localhost', port))

	def send(self):
		self.clientsocket.send('hello')

def main():
	import socket

	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('localhost', 8089))
	clientsocket.send('hello')

if __name__ == "__main__":
	main()