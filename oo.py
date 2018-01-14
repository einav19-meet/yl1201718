from turtle import *
import random
import time

colormode(255)
tracer(0)
hideturtle()

class Circle(Turtle):
	def __init__(self,x,y,dx,dy,radius):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
	 	self.radius = radius
		
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)

	def move(self, screen_width, screen_hight):
		curentx = self.xcor()
		curenty = self.ycor()
		new_x = curentx + dx
		new_y = curenty + dy
		right_side_ball = new_x+radius
		left_sida_ball = new_x-radius
		top_side_ball = new_y+radius
		bottom_side_ball = new_y+radius
		self.goto(curentx + self.dx,curenty + self.dy)