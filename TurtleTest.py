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



import turtle,random,math

turtle.delay(0)

def createTortues():
    tortues=[]
    for i in range(5):
        maTortue=turtle.Turtle()
        maTortue.speed(0.1)
        maTortue.color(random.random(),random.random(),random.random())
        tortues.append(maTortue)
    return tortues

def tourne(tortue):
    var=random.randint(0,2)
    if var==0:
        tortue.left(10)
    if var==2:
        tortue.right(10)

def printDistance(a):
    print(math.sqrt(a.xcor()*a.xcor()+a.ycor()*a.ycor()))

tortues=createTortues()
count=0
while True:
    for i in tortues:
        count+=1
        tourne(i)
        i.forward(1)
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
