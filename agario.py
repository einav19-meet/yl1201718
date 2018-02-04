import turtle
from turtle import *
import random
import time
import math
from project import ball
colormode(255)
tracer(0)
hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

SCORE=0

MY_BALL = ball(0,0,10,10,15,'red')

NUMBER_OF_BALLS = 7
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 20
MINIMUM_BALL_DX = (-1)
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = (-1)
MAXIMUM_BALL_DY = 1

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx =random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	dy =random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
	
	new_ball=ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls():
	for ball_1 in BALLS:
		ball_1.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_1,ball_2):
	if ball_1==ball_2:
		return False
	D=math.sqrt(math.pow(ball_2.xcor()-ball_1.xcor(),2)+math.pow(ball_2.ycor()-ball_1.ycor(),2))
	if ball_1.radius+ball_2.radius >= D+10:
		return True 
	else:
		return False

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
				new_ball_color = (new_r,new_g,new_b)

				while (new_ball_dx==0):
					new_ball_dx =random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				while (new_ball_dy==0):
						new_ball_dy =random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))

				if(ball_1_radius>ball_2_radius):
					ball_2.goto(x,y)
					ball_2.dx = new_ball_dx
					ball_2.dy = new_ball_dy
					ball_2.radius = new_ball_radius
					ball_2.color(new_ball_color)

					ball_2.shapesize(new_ball.radius/10)

					ball_1.radius = ball_1.radius+1
					ball_1.shapesize(ball_1.radius/10)

				if(ball_2_radius>ball_1_radius):
					ball_1.goto(x,y)
					ball_1.dx = new_ball_dx
					ball_1.dy = new_ball_dy
					ball_1.radius = new_ball_radius
					ball_1.color(new_ball_color)

					ball_1.shapesize(new_ball.radius/10)

					ball_2.radius = ball_2.radius+1
					ball_2.shapesize(ball_2.radius/10)


def check_nyball_collision():
	

	for ball in BALLS:
		if collide(MY_BALL,ball):
			ball_radius = ball.radius
			my_ball_radius = MY_BALL.radius

			if ball_radius > my_ball_radius:
				global SCORE 
				print("game over")
				clear()
				pu()
				goto(200,0)
				write("game over",align='right',font=('Ariel',50,'bold'))
				pu()
				SCORE +=1
				pu()
				goto(250,150)
				write(SCORE,align = 'right',font=('Ariel',20,'normal'))
				write("your final score: "+str(SCORE),align='right',font=('Ariel',20,'normal'))

				return False

			else:

				screen_xpos = random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH- MAXIMUM_BALL_RADIUS))
				screen_ypos = random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS))
				
				ball_dx = random.randint(int(MAXIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				while ball_dx==0:
						ball_dx = random.randint(int(MAXIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				ball_dy = random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				while ball_dy==0:
					ball_dy = random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				ball_radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
				while ball_radius==0:
					ball_radius = random.randint(int(MINIMUM_BALL_RADIUS),int(MAXIMUM_BALL_RADIUS))
				new_r = random.randint(0,255)
				new_g = random.randint(0,255)
				new_b = random.randint(0,255)
				ball_color = (new_r,new_g,new_b)

				
				ball.goto(screen_xpos,screen_ypos)
				ball.dx = ball_dx
				ball.dy = ball_dy
				new_ball.radius = ball_radius
				new_ball.color(ball_color)

				

				my_ball_radius = my_ball_radius+1

				clear()
				SCORE +=1
				pu()
				goto(-250,150)
				write(SCORE,align = 'right',font=('Ariel',20,'normal'))

	return True


def movearound(event):
	MY_BALL.goto(event.x- SCREEN_WIDTH,SCREEN_HEIGHT- event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()

while RUNNING==True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2:
	 	SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2

	if SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2



	move_all_balls()
	check_all_balls_collision()

	if check_nyball_collision()==False:
		RUNNING=False
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()