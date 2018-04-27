import math
class point():

	def __init__(self,c=10,d=5):
		self.l=c
		self.b=d

center=point()
print(center.l)
print(center.b)

def distance():
	z = math.sqrt(center.l*2 - center.b*2)
	print(z)

distance()
