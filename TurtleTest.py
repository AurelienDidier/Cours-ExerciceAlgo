import turtle, random

def turn(man):
    if random.randint(0,1)==0:
        man.left(90)
    else:
        man.right(90)

man=turtle.Turtle()
man.speed(1)
turtle.delay(0)
man.forward(5)
while True:
    turn(man)
    man.forward(5)

"""def turn(man):
    man.left(random.randint(0,360))
"""
