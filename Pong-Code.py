# Playable Pong Game in Python 3 for Beginners
# Pong Game Deluxe - Updated by TJ Martin and Taylor Harbin


import turtle
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
paddle_a.color("lime")
# Stretching the paddle to the appropriate length
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# Paddle starting position (left side)
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("lime")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# Paddle starting position (right side)
paddle_b.goto(350, 0)

# Ball
# Keep original size and start in the middle of the screen
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lime")
ball.penup()
ball.goto(0, 0)
# Speed of the ball
ball.dx = .125  
ball.dy = .125

# Pen (Scoreboard)
pen = turtle.Turtle()
pen.speed(0)
pen.color("lime")
# Gets rid of line that is drawn on the screen
pen.penup()
# Hides the drawing animation
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

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

# Keyboard binding
wn.listen()
# Call the function when the corresponding key is pressed
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()	

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Y Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # X Border Checking
    if ball.xcor() > 360:
        ball.goto(0, 0)
        ball.dx *= -1
        # Function to add a score to player 1
        score_a += 1
        # Clears previous score
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -360:
        ball.goto(0, 0)
        ball.dx *= -1
        # Function to add a score to player 2
        score_b += 1
        # Clears previous score
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    # Set up for the ball to be able to collide with the paddles but not the x-axis borders
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1
    
