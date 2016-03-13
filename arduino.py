import bluetooth
def main():
	mod1_addr = "98:D3:31:FC:0E:DC"
	port = 1
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((mod1_addr, port))
	sock.send("hello!!")
	sock.close()

def printDevices():
	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		print bdaddr
		print bluetooth.lookup_name( bdaddr )

if __name__ == "__main__":
	main()