#drawing a square using the turtle module
import turtle as t
def  rectangle(length):
    """using iteration to draw shape"""
    for i in range(4):
        t.fd(length)
        t.rt(90)
        t.exitonclick()
    

rectangle(60)
rectangle(120)
rectangle(180)
rectangle(240)