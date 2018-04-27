import math
class rectangle():

        def __init__(self,c=10,d=5,e=5):
                self.w=c
                self.h=d
		self.c=e

center=rectangle()
print(center.w)
print(center.h)
print(center.c)

#def rectangle_fn():
#	z = math.sqrt(center.l*2 - center.b*2)
#	print(z)

def find_center():
	p = rectangle()
	p.x = center.c + center.h/2
	p.y = center.c + center.w/2
	return p

rectangle_fn()
