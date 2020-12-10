# Playable Pong Game in Python 3 for Beginners
# Pong Game Deluxe - Updated by TJ Martin and Taylor Harbin


import turtle
import winsound
# Setting the Frames Per Second
FPS = 60 

wn = turtle.Screen()
wn.title("Pong Game Deluxe")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score (At the start of game)
score_a = 0
score_b = 0

# Paddle A
# paddle_x = modulename.Classname
paddle_a = turtle.Turtle()
# Setting the paddle to maximum possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("purple")
# Stretching the paddle to the appropriate length
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# Paddle starting position (left side)
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# Paddle starting position (right side)
paddle_b.goto(350, 0)

# Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("purple")
paddle_c.shapesize(stretch_wid=1, stretch_len=5)
paddle_c.penup()
# Paddle starting position (middle)
paddle_c.goto(0, 250)

#Paddle D
paddle_d = turtle.Turtle()
paddle_d.speed(0)
paddle_d.shape("square")
paddle_d.color("blue")
paddle_d.shapesize(stretch_wid=1, stretch_len=5)
paddle_d.penup()
#Paddle starting position(middle)
paddle_d.goto(0,-250)


# Ball
# Keep original size and start in the middle of the screen
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
# Speed of the ball
ball.dx = .155  
ball.dy = .155

# Pen (Scoreboard)
pen = turtle.Turtle()
pen.speed(0)
pen.color("lime")
# Gets rid of line that is drawn on the screen
pen.penup()
# Hides the drawing animation
pen.hideturtle()
pen.goto(0, 260)
pen.write("Lakers: 0  Clippers: 0", align="center", font=("Courier", 24, "normal"))

# Function

def paddle_a_up():
    # Return the y-coordinates and store it in variable 'y'
	y = paddle_a.ycor()
    # Move the paddle up by 22 pixels
	y += 22
    # Update new coordinates 
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 22
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 22
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 22
	paddle_b.sety(y)

def paddle_c_left():    
    x = paddle_c.xcor()
    x += 22
    paddle_c.setx(x)

def paddle_c_right():
    x = paddle_c.xcor()
    x -= 22
    paddle_c.setx(x)

def paddle_d_left():
    x = paddle_d.xcor()
    x -= 22
    paddle_d.setx(x)

def paddle_d_right():
    x = paddle_d.xcor()
    x += 22
    paddle_d.setx(x)

# Keyboard binding
wn.listen()
# Call the function when the corresponding key is pressed
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_c_left, "y")
wn.onkeypress(paddle_c_right, "t")
wn.onkeypress(paddle_d_left, "v")
wn.onkeypress(paddle_d_right, "b")
# Main game loop
while True:
    wn.update()	

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Y Border checking (deleted for 4 player mode)
    if ball.ycor() > 270:
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        #Function to add a score to Team 2 (Clippers)
        score_b += 1
        #Clears previous score
        pen.clear()
        pen.write("Lakers: {}  Clippers: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.ycor() < -290:
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dy *= -1
        #Function to add a score to team 1 (Lakers)
        score_a += 1
        #Clears previous score
        pen.clear()
        pen.write("Lakers: {}  Clippers: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # X Border Checking
    if ball.xcor() > 360:
        ball.goto(0, 0)
        ball.dx *= -1
        # Function to add a score to Team 1 (Lakers)
        score_a += 1
        # Clears previous score
        pen.clear()
        pen.write("Lakers: {}  Clippers: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -360:
        ball.goto(0, 0)
        ball.dx *= -1
        # Function to add a score to Team 2 (Clippers)
        score_b += 1
        # Clears previous score
        pen.clear()
        pen.write("Lakers: {}  Clippers: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    # Set up for the ball to be able to collide with the paddles but not the x-axis borders
    #Paddle B Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pongblip.wav", winsound.SND_ASYNC)

    # Paddle A Collision
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pongblip.wav", winsound.SND_ASYNC)
    
    # Paddle C Collision
    elif (ball.ycor() > 240 and ball.ycor() < 250) and (ball.xcor() < paddle_c.xcor() + 60 and ball.xcor() > paddle_c.xcor() -60):
        ball.sety(240)
        ball.dy *= -1
        winsound.PlaySound("pongblip.wav", winsound.SND_ASYNC)
    
    #Paddle D Collision
    elif (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle_d.xcor() + 60 and ball.xcor() > paddle_d.xcor() -60):
        ball.sety(-240)
        ball.dy *= -1
        winsound.PlaySound("pongblip.wav", winsound.SND_ASYNC)


   
 