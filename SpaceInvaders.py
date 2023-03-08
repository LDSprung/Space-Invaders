#import libraries
import turtle 
import time 
import random 

currentTime = time.time()

score = 0
highScore = 0

#define the game window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#define the player character
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.turtlesize(1, 2)
player.penup()
player.goto(0, -200)

#define the player projectile
pew = turtle.Turtle()
pew.speed(0)
pew.shape("circle")
pew.color("white")
pew.turtlesize(0.5, 0.5)
pew.penup()

#bullet state and game state variables
pewState = "ready"
game = "start"

#create array of enemy ships
enemy = []
for i in range(1, 6):
    newEnemy = turtle.Turtle()
    newEnemy.speed(0)
    newEnemy.shape("triangle")
    newEnemy.color("red")
    newEnemy.tiltangle(30)
    newEnemy.turtlesize(1.5, 1.5)
    newEnemy.penup()
    x = random.randint(-380, 380)
    newEnemy.goto(x, 250)
    enemy.append(newEnemy)

#define the scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#define the movement for the player
def movLeft():
    x = player.xcor()
    player.setx(x - 20)

def movRight():
    x = player.xcor()
    player.setx(x + 20)

#on spacebar, set the bullet just above the player position
def shoot():
    global pewState
    pewState = "fire"
    x = player.xcor()
    y = player.ycor() + 10
    pew.goto(x, y)

#reset the game when you lose
def reset():
    global game
    for e in enemy:
        e.hideturtle()
        e.goto(1500, 1500)

    enemy.clear()

    for i in range(1, 6):
        newEnemy = turtle.Turtle()
        newEnemy.speed(0)
        newEnemy.shape("triangle")
        newEnemy.color("red")
        newEnemy.tiltangle(30)
        newEnemy.turtlesize(1.5, 1.5)
        newEnemy.penup()
        x = random.randint(-380, 380)
        newEnemy.goto(x, 250)
        enemy.append(newEnemy)

    game = "start"

#keypress
wn.listen()
wn.onkeypress(movLeft, "a")
wn.onkeypress(movRight, "d")
wn.onkeypress(shoot, "space")
wn.onkeypress(reset, "r")

while True:
    #cap the framerate
    newTime = time.time()
    if newTime - currentTime < (1/60):
        continue
    else:
        currentTime = newTime

    wn.update()

    #move the enemy ships down the screen at a constant speed
    for e in enemy:
        if game == "start":
            y = e.ycor()
            y -= 0.5
            e.sety(y)
            
            #if an enemy ship reaches the player, stop the game, and reset the score
            if e.ycor() < -200:
                game = "stop"
                score = 0
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    #define player collision with borders
    if player.xcor() < -380:
        player.goto(-380, -200)
    elif player.xcor() > 380:
        player.goto(380, -200)
    
    #movement of the projectile
    if pewState == "fire":
        y = pew.ycor()
        y += 10
        pew.sety(y)
    
    #define interaction between enemy ship and projectile       
    for j in enemy:
        #remove both the enemy ship and the projectile from the screen
        if j.distance(pew) < 20:
            pewState = "ready"
            pew.goto(1000,1000)
            j.goto(1500,1500)
            enemy.remove(j)

            #increase the score
            score += 10

            #add to the high score if the current score is better
            if score > highScore:
                highScore = score

            #update the score board
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

            #create a new ship at a random spot at the top of the screen
            newEnemy = turtle.Turtle()
            newEnemy.speed(0)
            newEnemy.shape("triangle")
            newEnemy.color("red")
            newEnemy.tiltangle(30)
            newEnemy.turtlesize(1.5, 1.5)
            newEnemy.penup()
            x = random.randint(-380, 380)
            newEnemy.goto(x, 250)
            enemy.append(newEnemy)
    
wn.mainloop()