from turtle import*
import turtle     
import math                                                                         

class ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1=ball(10, "red",10)
ball2=ball(30,"blue",15)

def dist (ball1,ball2):
	ball1x = ball1.xcor()
	ball1y = ball1.ycor()
	ball2x = ball2.xcor()
	ball2y = ball2.ycor()
dis = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
print(dis)


def check_collision(ball1,ball2,dist):
	if ball1.radius+ball2.radius>dist():
		print("DANGER! THE BALLS ARE COLLAIDING")
mainloop()