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
	for ball_1 in BALLS:
		ball_1.move(SCREEN_HEIGHT,SCREEN_WIDTH)

def collide(ball_a,ball_b):
	if ball_1=ball_2:
		return False
	if ball_1.radius+ball_2.radius > math.sqrt(math.pow(ball_2.xcor()-ball_1.xcor()),2)+math.pow((ball_2.ycor()-ball_1.ycor()),2)):
	return True 
	else return False

def check_all_balls_collision():
	for ball_1 in BALLS:
		for ball_2 in BALLS:
			if collide(ball_1,ball_2):
				ball_1_radius = ball_1.radius
				ball_2_radius = ball_2.radius
				new_ball_x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				new_ball_y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				new_ball_dx =random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				new_ball_dy =random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				new_ball_radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
				new_r = random.randint(0,255)
				new_g = random.randint(0,255)
				new_b = random.randint(0,255)
				new_color = (new_r,new_g,new_b)

				while (new_ball_dx==0):
					new_ball_dx =random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				while (new_ball_dy==0):
						new_ball_dy =random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))

				if(ball_1_radius>ball_2_radius):
					ball_2.











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