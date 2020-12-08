"""
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
"""



import turtle, random, math
def turn(man):
    var= random.randint(0,2)
    if var==0:
        man.left(90)
    if var==2:
        man.right(90)
"""
def turn(man):
    man.left(random.randint(0,360))
"""

def printDistance(a):
    print(math.sqrt(a.xcor()*a.xcor()+a.ycor()*a.ycor()))

def addNewRandomWalk(list):
    man=turtle.Turtle()
    man.speed(1)
    man.color(random.random(),random.random(),random.random())
    return list.append(man)
[]
list=[]
turtle.delay(0)
for i in range(4):
    addNewRandomWalk(list)

count=0
while True:
    count+=1
    for i in list:
        turn(i)
        i.forward(10)
        if (count==10):
            printDistance(i)
        if (count==50):
            printDistance(i)
        if (i==100):
            printDistance(i)
        if (i==200):
            printDistance(i)
        if (count==500):
            printDistance(i)
        if (count==1000):
            printDistance(i)
        if (count==2000):
            printDistance(i)
        if (count==3000):
            printDistance(i)

