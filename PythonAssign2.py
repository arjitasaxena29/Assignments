
##PROGRAM_1

def generate_n_chars(n,c):
        for i in range(0,n):
            print(c, end='')

a=int(input("Enter a num: "))
b=input("Enter a char: ")
generate_n_chars(a,b)


##PROGRAM_2

def max_in_list(n):
        max=0
        for i in n:
                j=int(i)
                if j>max :
                        max=j
        print(max)
              
a=list(input("Enter the list: "))
max_in_list(a)


##PROGRAM_3

a=(input("Enter the list: ")).split(',')
b=[]
for i in a:
        b.append(len(i))
print(b)


##PROGRAM_4

a=(input("Enter the list of words: ")).split(',')
max=0
for i in a:
        l=len(i)
        if l>max:
                max=l
print(max)


##PROGRAM_5

a=(input("Enter the list of words: ")).split(',')
n=int(input("Enter a num: "))

def filter_long_words(a,n):
        b=[]
        for i in a:
                l=len(i)
                if l>n:
                        b.append(i)
        print(b)
                
filter_long_words(a,n)


##PROGRAM_6

import string
a=string.punctuation
b=input("Enter phrase: ")
word=''.join([x for x in b.lower() if not x in a]).replace(' ','')
r=word[::-1]
print("{0} in reverse is {1}".format(word,r))
if r == word:
        print("Palindrome")
else:
        print("Not Palindrome")


##PROGRAM_7

from string import ascii_lowercase

def pang(a):
        return set(ascii_lowercase)-set(s.lower())==set([])
s=input("Enter String: ")
if(pang(s)==True):
        print("It is a Pangram!")
else:
        print("It is not a Pangram!")


##PROGRAM_8

d={"merry":"god","christmas":"jul", "and":"och","happy":"gott", "new":"nytt","year":"as" }
print(d['merry'])

def translate(e):
        l=[]
        for i in e:
                l.append(d.get(i))
        print(l)

a=(input("Enter list")).split(',')
translate(a)


##PROGRAM_9

def char_freq(s):
        d={}
        for i in s:
                if i in d.keys():
                        d[i]+=1
                else:
                        d[i]=1
        print(d)       
s=list(input("Enter a string: "))
print(s)
char_freq(s)


## PROGRAM_10

#MODULE-(Mathematics.py)

def add1(a,b):
    s=([(int(i)+int(j)) for i,j in zip(a,b)])
    return s

def sub1(a,b):
    s=([(int(i)-int(j)) for i,j in zip(a,b)])
    return s

def max1(c):
    m=max(c)
    return m

def sort1(c):
    c.sort()
    return c

#(MathematicsFile.py)

import Mathematics

a=list(input("Enter a: "))
print(a)
b=list(input("Enter b: "))
print(b)

ad=list(Mathematics.add1(a,b))
print('Addition is: ',ad)

sb=list(Mathematics.sub1(a,b))
print('Subtraction is: ',sb)

mx=int(Mathematics.max1(ad))
print('Maximum value is: ',mx)

sr=list(Mathematics.sort1(ad))
print('Sorted list is: ',sr)


## PROGRAM_11

#PACKAGE-(MyPackage)

#MODULE-(Mathematics.py)

def add1(a,b):
    s=([(int(i)+int(j)) for i,j in zip(a,b)])
    return s

def sub1(a,b):
    s=([(int(i)-int(j)) for i,j in zip(a,b)])
    return s

def max1(c):
    m=max(c)
    return m

def sort1(c):
    c.sort()
    return c

#(MathematicsFile.py)
import MyPackage.Mathematics.*

a=list(input("Enter a: "))
print(a)
b=list(input("Enter b: "))
print(b)

ad=list(add1(a,b))
print('Addition is: ',ad)

sb=list(sub1(a,b))
print('Subtraction is: ',sb)

mx=int(max1(ad))
print('Maximum value is: ',mx)

sr=list(sort1(ad))
print('Sorted list is: ',sr)


## PROGRAM_12

class date:
        import datetime
        dt=datetime.datetime.now()
        def __init__(self):
                self.y=date.dt.year
                pass

        def displayTime(self):
                print("time-{0}:{1}:{2}".format(date.dt.hour,date.dt.minute,date.dt.second))

        def displayDate(self):
                print("date-{0}/{1}/{2}".format(date.dt.day,date.dt.month,date.dt.year))

class usedate:
        def __init__(self):
                d=date()
                d.displayTime()
                d.displayDate()
                
usedate()


## PROGRAM_13

file=open("emps.txt",'r')
data=file.read()
file.close()

a=data.split(',')
id=a[0]
name=a[1]
sal=a[2]

b=open("test.txt",'w')
b.write(str(id)+','+name+','+str(sal))
print("New file created with existing data ")
print("id:{0} name:{1} salary:{2}".format(id,name,sal))
b.test(str(id)+","+str(name)+","+str(sal))
b.close()


## PROGRAM_14

import math
print(dir(math))
import numpy
print(dir(numpy))



