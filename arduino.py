import bluetooth
import sys
import time

#Bluetooth address
mod1_addr = "98:D3:31:FC:0E:DC"
port = 1



def main():
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((mod1_addr, port))

	#The data to be sent
	word = "Anton#"
	for letter in word:
		if letter == "#":
			print "Message sent correctly."
			return 0

		print "Send message " + letter

		message = ""
		KsKr = False
		while(not KsKr):
			try:
				print "Ks" + letter
				sock.send("Ks" + letter)
				try:
					message = message + sock.recv(32)

					if ("Kr" + letter) in message:
						print message
						#Sender knows that the receiver knows
						KsKr = True
				except Exception:
					import traceback
					traceback.print_exc()
					KsKr = True
			except bluetooth.BluetoothError:
				reconnect(sock, mod1_addr, port)
			time.sleep(1)


		print "KsKr" + letter
		time.sleep(1)
		message = ""
		KsKrKsKr = False
		while(not KsKrKsKr):
			try:
				print "KsKr" + letter
				sock.send("KsKr" + letter)
				try:
					message = message + sock.recv(32) #Receive 32 bits
					print message
					if ("KrKsKr" + letter) in message:
						print "KsKrKsKr" + letter
						#Sender knows that the receiver knows ...
						KsKrKsKr = True
				except Exception:
					import traceback
					traceback.print_exc()
			except bluetooth.BluetoothError:
				reconnect(sock, mod1_addr, port)
	sock.close()

	return 0

def reconnect(sock, mod1_addr, port):
	sock.close()
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((mod1_addr, port))
	print "reconnected"

def printDevices():
	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		print bdaddr
		print bluetooth.lookup_name( bdaddr )
		# NOTE to self check signal strength:
		# sudo rfcomm connect 0 98:D3:31:FC:0E:DC >/dev/null &
		# hcitool rssi 98:D3:31:FC:0E:DC

if __name__ == "__main__":
	main()
	#printDevices()