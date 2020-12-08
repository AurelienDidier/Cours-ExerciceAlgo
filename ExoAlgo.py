import random
#A 1

def sum(a,b):
    return a+b

def oppose(a):
    return -1*a

def waitInteger():
    try:
        int(input("Entrer un nombre entier: "))
        return True
    except ValueError:
        return False

def isBissextile(annee):
    if annee%4==0 and annee%100!=0:
        return True
    elif annee%400==0:
        return True
    else:
        return False

def isBissextil(annee):
    return annee%4==0 and annee%100!=0 or annee%400==0

def sumNumber(a):
    if a>10:
       return a%10 + a//10
    else:
       return 10

def isValidCardNumber(nombre):
    s=str(nombre)
    res=0
    for i in s[::2]:
        res += sumNumber(int(i))
    for i in s[1::2]:
        res = sumNumber(int(i)*2)
    return res%10==0

#print(isValidCardNumber(8537))

def guessNumber():
    toGuess=random.randint(0,1000)
    var=-1
    count=0
    while var!=toGuess:
        var=int(input("Guess the number:"))
        count+=1
        if (var<toGuess):
            print("C'est plus.")
        if (var>toGuess):
            print("C'est moins.")
    print("Gagné en "+ str(count) + " coup!")

#guessNumber()

#B

def first(list):
    return list[0]

def last(list):
    return list[-1]

def initListe(n):
    return list(range(0,n+1))

def contain(list,n):
    for i in liste:
        if i==n:
            return True
    return False

def mean(list):
    res=0
    for i in list:
        res+=i
    return res/len(list)

def occurs(list,n):
    occ=0
    for i in list:
        if i==n:
            occ+=1
    return occ

def contains(list1,list2):
    for i in list2:
        if not contain(list1,i):
            return False
    return True

def initMultTable(n):
    list=[]
    for i in range(n):
        list.append([])
        for j in range(n):
            list[i].append(i*j)
    return list

#print(initMultTable(5))
