from turtle import *

# def draw_attractive_design2():
#     colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#     pen = turtle.Turtle()
#     pen.speed(10)
#     turtle.bgcolor("black")  
#     pen.pensize(2)

#     initial_size = 30  

#     for i in range(200):
#         pen.color(colors[i % 6])
#         pen.forward(initial_size + i)
#         pen.left(59)

#     pen.hideturtle()


# draw_attractive_design2()


# turtle.done()

#*heart sign 
# begin_fill()
# color("red","purple")
# left(50)
# forward(100)
# circle(40,180)
# left(260)
# circle(40,180)
# forward(100)
# end_fill()
# done()


#*F
from turtle import *

Screen().bgcolor('black')

t= Turtle()
t.pencolor('red')

t.color("white", "white")
t.left(90)
t.forward (40)
t.right(90)
t.circle(40, 90)
t.forward(80)
t.circle(20, 180)
t.right(180)
t.circle(20, 180)
t.right(180)
t.forward(80)
t.circle(20,180)
t.forward(80)
t.right(180)
t.circle(20,180)
t.forward(80)
t.right(180)
t.penup()
t.forward(40)
t.pendown()
t.circle(20,180)
t.left(50)
t.forward(50)
t.right(50)
t.circle(40,90)
t.right(90)
t.forward(40)
t.left(90)
t.forward(80)

done()
