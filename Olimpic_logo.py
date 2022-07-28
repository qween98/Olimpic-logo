import turtle
t = turtle.Turtle()
t.speed(0)
def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def circle():
    for i in range(60):
        t.forward(5)
        t.left(6)

def spiral():
    for i in range(500):
        t.forward(i / 10)
        t.left(15)

def star():
    for i in range(5):
        t.forward(100)
        t.left(144)

def olimpic_circle(x, y, color):
    t.color(color)
    t.width(10)
    move(x, y)
    circle()
        
#spiral()
#star()
def olimpic_logo():  
    olimpic_circle(-120, 60, "blue")
    olimpic_circle(0,60, "black")
    olimpic_circle(120, 60, "red")
    olimpic_circle(-60, 0, "yellow")
    olimpic_circle(60, 0, "green")


def upp():
    t.setheading(90)
    t.forward(10)
def down():
    t.setheading(-90)
    t.forward(10)
def right():
    t.setheading(0)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def up_or_down():
    if t.isdown():
        t.up()
    else:
        t.down()
    
def red():
    t.color("red")

def green():
    t.color("green")

def width():
    t.width(15)   

olimpic_logo()

t.screen.onkeypress(upp, "Up")
t.screen.onkeypress(down, "Down")
t.screen.onkeypress(right, "Right")
t.screen.onkeypress(left, "Left")
t.screen.onkeypress(up_or_down, "space")
t.screen.onkeypress(red, "r")
t.screen.onkeypress(green, "g")
t.screen.onkeypress(width, "q")

t.screen.listen()
t.screen.mainloop()














