class Dog:

	def __init__ (self, length, width):
		self.length = length
		self.width = width
	
	def get_length(self):
		return self.length
	def get_width(self):
		return self.width	

while True:
	print("Hello there, this is your first program in an executable")
	meta = Dog(10, 20)
	print("This is the width of meta" , meta.get_width())
	text = input("type any key to exit")
	if text != "":
		break
