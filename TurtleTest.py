import turtle,random,math

turtle.delay(0)

def createTortues(n):
    tortues=[]
    for i in range(n):
        maTortue=turtle.Turtle()
        maTortue.speed(0.1)
        maTortue.color(random.random(),random.random(),random.random())
        tortues.append(maTortue)
    return tortues

def tourne(tortue, angle):
    var=random.randint(0,2)
    if var==0:
        tortue.left(angle)
    if var==2:
        tortue.right(angle)

def printDistance(a):
    print(math.sqrt(a.xcor()*a.xcor()+a.ycor()*a.ycor()))

tortues=createTortues(5)
count=0
while True:
    for i in tortues:
        count+=1
        tourne(i,90)
        i.forward(5)
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
