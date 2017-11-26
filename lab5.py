from turtle import*
import random
colormode(255) 
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		red=random.randint(0,256)
		green=random.randint(0,256)
		blue=random.randint(0,256)
		self.color((red,green,blue))
square1=Square(size=10)
square1.random_color()
print(square1)
random.randint(0,256)


