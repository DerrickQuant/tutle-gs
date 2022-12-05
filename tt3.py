#colorful spiral
import turtle as t
colors = ["blue", "green", "red", "orange", "magenta", "violet"]
 #causes drawing to appear almost immediately t.tracer(0,0)
for i in range(45):
    t.color(colors[i % 6])
    t.pendown()
    t.fd(2 + i * 5)
    t.left(45)
    t.width(i)
    t.penup()

