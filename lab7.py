from turtle import*
import random   
import math                                                                         

class ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.radius = radius
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1=ball(1, "red",1)
ball1.pu()
ball1.goto(100,0)
ball1.pd()
ball2=ball(3,"blue",1)
ball2.pu()
ball2.goto(61,0)
ball2.pd()

	
ball1x = ball1.xcor()
ball1y = ball1.ycor()
ball2x = ball2.xcor()
ball2y = ball2.ycor()

def check_collision(ball1,ball2):
	if (ball1.radius)*10+(ball2.radius)*10 > math.sqrt((ball2x - ball1x)**2 + (ball2y - ball1y)**2):
		print("DANGER! THE BALLS ARE COLLAIDING")

check_collision(ball1,ball2)
mainloop()