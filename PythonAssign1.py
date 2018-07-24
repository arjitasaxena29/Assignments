#Prog_1

name=input("Enter your name: ")
print('Hello', name)
print('Hello,',name)


#Prog_2

n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))

s1=n1+n2

if s1>=0 :
    print('Sum is positive')
else:
    print('Sum is negative')


#Prog_3
    
n1=int(input("Enter a niumber to be stored: "))
n2=int(input('Enter number:'))

while(True):
    
    if n2!=n1:
        n2=int(input('Enter number:'))
    else:
        print("Correct!")
        break


#Prog_4
    
firstname=input("Enter first name: ")
lastname=input("Enter last name: ")
wholename= ("{0}.{1}".format(firstname,lastname))
print(wholename)


#Prog_5

str=input("Enter a string: ")
print(str.swapcase())


#Prog_6

l=(input("Enter list: ")).split(',')
sum1=0
multi1=1

for i in l:
    sum1=sum1+int(i)
    
    multi1=multi1*int(i)

print(sum1)
print(multi1)


#Prog_7

x=input("Enter a value")
a=list(input("Enter the list"))
flag=0
i=0
while i<=a:
    if x==i:
        flag=1
        print("True")
        break
    else:
        i=i+1
        continue
        
if flag==0:
    print("False")


#Prog_8

a=list(input("Enter the list1: "))
b=list(input("Enter the list2: "))
flag=0
for i in a:
    for j in b:
        if i==j:
            flag=1
            print("True")
            break
        else:
            continue
        
    if flag==1:
         break
if flag==0:
    print("False")


#Prog_9

h=(input("Enter list")).split(',')
x1='*'
i=0
while i < len(h):
    print(x1*int(h[i]))
    print("\r")
    i=i+1
