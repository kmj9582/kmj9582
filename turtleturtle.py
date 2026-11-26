import turtle
import time
turtle.shapesize(0.1)
turtle.speed(0)
k = 180
turtle.right(50)
for colours in ["purple","greenyellow","crimson","sienna","cyan","limegreen"
                ,"springgreen","slategray","orangered","red","goldenrod","blueviolet"
                ,"mediumpurple","deepskyblue","gold","slategrey","navy"]:
    turtle.color(colours)
    turtle.fillcolor(colours)
    turtle.begin_fill()
    for j in range(10):
        turtle.forward(k)
        turtle.right(360/10)
    k -= 10
    turtle.end_fill()
    turtle.right(20)
time.sleep(5)