import bluetooth
import sys
import time

def main():
	mod1_addr = "98:D3:31:FC:0E:DC"
	port = 1
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((mod1_addr, port))

	# sudo rfcomm connect 0 98:D3:31:FC:0E:DC >/dev/null &
	# hcitool rssi 98:D3:31:FC:0E:DC


	word = "Anton#"
	for letter in word:
		print "Send message " + letter

		message = ""
		KsKr = False
		while(not KsKr):
			sock.send("Ks" + letter)
			try:
				message = message + sock.recv(32)

				if ("Kr" + letter) in message:
					print message
					KsKr = True
			except Exception:
				import traceback
				traceback.print_exc()
				KsKr = True
			time.sleep(1)


		print "KsKrA"
		time.sleep(3)
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


def printDevices():
	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		print bdaddr
		print bluetooth.lookup_name( bdaddr )
		bluetooth.
if __name__ == "__main__":
	main()
	#printDevices()