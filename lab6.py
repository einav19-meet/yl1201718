from turtle import*
class Rectangle(Turtle):
	def __init__(self,hight,width):
		Turtle.__init__(self)
		register_shape("Rectangle",((int(width),0),(int(width),int(hight)),(0,int(hight)),(0,0)))
		self.shape("Rectangle")
		self.width = width
		self.hight = hight
Rectangle1=Rectangle(20,10)
print(Rectangle1)

mainloop()