import socket

class server():
	serversocket = None

	def __init__(self, port=None):
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind(port)
		self.listen()
		return self.serversocket

	def bind(self, port):
		self.serversocket.bind(('localhost', port))

	def listen(self):
		self.serversocket.listen(5) # become a server socket, maximum 5 connections

		while True:
			connection, address = self.serversocket.accept()
			buf = connection.recv(64)
			if len(buf) > 0:
				print buf
				break
