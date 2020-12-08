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

""" A plusieurs
import turtle, random

def turn(man):
    var= random.randint(0,2)
    if var==0:
        man.left(90)
    if var==2:
        man.right(90)

def addNewRandomWalk(list):
    man=turtle.Turtle()
    man.speed(1)
    man.color(random.random(),random.random(),random.random())
    return list.append(man)

list=[]
turtle.delay(0)

for i in range(4):
    addNewRandomWalk(list)

while True:
    for i in list:
        turn(i)
        i.forward(5)
"""
