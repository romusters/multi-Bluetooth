import receiver
import sender

class bluetoothModule():

	def __init__(self, id=None, message=None):
		self.message = message
	state = 1 #1 is sender 0 is receiver
	Ks = 0
	Kr = 0
	KsKr = 0
	KrKsKr = 0
	KsKrKsKr = 0
