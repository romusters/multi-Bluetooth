import bluetooth
import sys


def main():
	mod1_addr = "98:D3:31:FC:0E:DC"
	port = 1
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((mod1_addr, port))



	sock.send("Ksa")
	letter = "a"
	print "Send message"


	message = ""
	KsKr = False
	while(not KsKr):
		try:
			message = message + sock.recv(32)
			print message
			if ("Kr" + letter) in message:
				KsKr = True
		except Exception:
			import traceback
			traceback.print_exc()
			KsKr = True

	print "KsKr established."
	message = ""
	KsKrKsKr = False
 	while(not KsKrKsKr):
		sock.send("KsKr" + letter)
		try:
			message = message + sock.recv(32)
			print message
			if ("KrKsKr" + letter) in message:
				print "Victory"
				KsKrKsKr = True
		except Exception:
			import traceback
			traceback.print_exc()
			KsKrKsKr = True

	sock.close()
	return 0

	#
	# recsock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	# port = 1
	# recsock.bind(("",port))
	# print recsock.listen(port)
	#
	# client_sock, address = recsock.accept()
	# print "Accepted connection from ", address
	#
	# data = client_sock.recv(1024)
	# print "received [%s]" % data
	# recsock.close()

def printDevices():
	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		print bdaddr
		print bluetooth.lookup_name( bdaddr )

if __name__ == "__main__":
	main()
	#printDevices()