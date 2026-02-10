import turtle   
turtle = turtle.Turtle()
turtle.speed(0)
turtle.color("blue")
turtle.pensize(5)   
# Draw a pattern using turtle graphics
for i in range(36):
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
# End of the pattern
# Hide the turtle   
obj1 = turtle.getscreen()
obj1.mainloop()
