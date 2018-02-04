import turtle
from turtle import *
colormode(255)
import random
import time

class ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
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
		new_x = curentx + self.dx
		new_y = curenty + self.dy
		right_side_ball = new_x+self.radius
		left_sida_ball = new_x-self.radius
		top_side_ball = new_y+self.radius
		bottom_side_ball = new_y-self.radius
		self.goto(curentx + self.dx,curenty + self.dy)

		if right_side_ball >= screen_width:
			self.dx = self.dx*-1

		if left_sida_ball <= -screen_width:
			self.dx = self.dx*-1

		if top_side_ball >= screen_hight:
			self.dy = self.dy*-1

		if bottom_side_ball <= -screen_hight:
			self.dy = self.dy*-1

