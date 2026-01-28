from turtle import Turtle, Screen
import random
screen = Screen()

race_start = False
turtle_x = -240
turtle_y = -120
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
user_bet = screen.textinput(title="Make your bets", prompt="Enter your Turtle`s color :")
turtles = []


for turtle in range(0,6):
    new_turtule = Turtle()
    new_turtule.penup()
    new_turtule.shape("turtle")
    new_turtule.color(colors[turtle])
    new_turtule.goto(x=turtle_x, y=turtle_y)
    turtle_y += 50
    turtles.append(new_turtule)

if user_bet:
    race_start = True
while race_start:
    for turtle in turtles:
        if turtle.xcor() > 220:
            race_start = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You`re win! The winner is {winner_color}")
            else:
                print(f"You`re lost! The winner is {winner_color}")
        distance = random.randint(0,10)
        turtle.fd(distance)








screen.exitonclick()