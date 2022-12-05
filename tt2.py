#creating a red flower
import turtle as t
t.bgcolor("yellow")
t.color("red")
t.pensize(10)
t.exitonclick
for angle in range(0, 360, 15):
    t.seth(angle)
    
    t.circle(100)
    t.exitonclick
