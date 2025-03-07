import turtle
import pygame

pygame.init()
bounce_sound = pygame.mixer.Sound("bounce_sound.wav")

wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# Ball Speed
ball_speed = 0.2

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed

 
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("arial", 22, "bold"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  
        y -= 20
        paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()
  
    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce_sound.play() 

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce_sound.play() 
       
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx = ball_speed  
        ball.dy = ball_speed
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("arial", 22, "bold"))

    elif ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx = -ball_speed 
        ball.dy = -ball_speed
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("arial", 22, "bold"))


    # Paddle ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350 and 
        ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1
        bounce_sound.play() 
       


    elif (ball.xcor() > 340 and ball.xcor() < 350 and 
          ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1
        bounce_sound.play() 
     
