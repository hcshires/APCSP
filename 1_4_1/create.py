class Aglets(object):
	def __init__(self, size=1, color="white", amount=0):
		''' Creates an aglet wit a size of 1-3 and any color '''
		self.amount = amount
		self.size = size
		self.color = color
		print("Add some aglets to the aglet army and TAKE OVER THE WORLD! They will be", size,"inches big and in", color)
		
	def add(self, add=1):
		''' Increases amount of aglets when called'''
		self.amount += add
		print("You now have", self.amount ,"aglets!")