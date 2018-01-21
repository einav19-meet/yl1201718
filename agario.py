import turtle
import random
import time
from project.py import ball

colormode(255)
tracer(0)
hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = ball(0,0,10,10,15,'red')

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = (-5)
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = (-5)
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range NUMBER_OF_BALLS:
	x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx =random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	dy =random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	self.color(r,g,b)
	ball_1=ball(x,y,dx,dy,radius,color)
	BALLS.Append(ball_1)

def move_all_balls():
	for ball_1 in BALLS():
		ball_1.move(SCREEN_HEIGHT,SCREEN_WIDTH)

def collide(ball_a,ball_b):
	if ball_a=ball_b:
		return False
	if ball_a.radius+ball_b.radius+10 > math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor()),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2)):
	return true 

	
math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))


my_x = random.randint(-100,100)
my_y = random.randint(-100,100)
circle1 = Circle(my_x,my_y,1,1,60)

my_x = random.randint(-100,100)
my_y = random.randint(-100,100)
circle2 = Circle(my_x,my_y,1,1,60) 

while True:
	circle1.move()
	circle2.move()
	getscreen().update()
	time.sleep(0.01)

mainloop()