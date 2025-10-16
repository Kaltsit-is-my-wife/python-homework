#1
s = input("请输入一个字符串：")
print("the string you have input is:",s)

i1 = int(input("请输入一个整数："))
print("the string you have input is:",i1)

#2
num = int(input("please input a number:"))
if num == 0:
    print("the number is zero")
elif num > 0:
    print("the number is positive")
else:
    print("the number is negative")

#3
i2 = 0
while i2 <= 10:
    print(i2,end = " ")
    i2 += 1

for i2 in range(11):
    print(i2,end = " ")

#4
i3 = 0
str = input("please input a string:")
while str[i3] != '\0':
    print(str[i3],end = " ")
    i3 += 1

for char  in str:
    print(char,end = " ")

#5
userList = []
continueInput = True
while continueInput:
    userInput = input("please input a string(enter 'exit' to stop):")
    if userInput == 'exit':
        continueInput = False
    else:
        userList.append(userInput)
print("the list you have input is:",userList)
l = [1,2,3,4,5]
t = (1,2,3,4,5)
print("the sum of l is:",sum(l))
print("the sum of t is:",sum(t))

#6
sum = float(sum(l))
avg = sum / len(l)
print("the average of l is:",avg)

#7
continueInput = True
while continueInput:
    i4 = int(input("please input a number between 1 ~ 100:"))
    if 1 <= i4 <= 100:
        print("the number you have input is:",i4)
        continueInput = False
    else:
        print("the number is out of range,please input again!")

#8
#e1.3TempConvert
def tempConvert(ValueStr):
    if ValueStr[-1]in ['F','f']:
        C =(eval(ValueStr[0:-1])-32)/1.8
        print("the temperature is:{:.2f}C".format(C))
    elif ValueStr[-1]in ['C','c']:
        F=1.8*eval(ValueStr[0:-1])+32
        print("the temperature is{:.2f}F".format(F))
    else:
        print("warning :wrong input!")
Tempstr =input("please input the value with temperature symbol：")

#9
#e2.1DrawPython
import turtle
turtle.setup(850,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(40)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)

#10
#e2.3DrawPython.py
import turtle
def drawSnake(radius,angle,length):
    turtle.seth(-40)
    for i in range(length):
        turtle.circle(radius,angle)
        turtle.circle(-radius,angle)
    turtle.circle(radius,angle/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40*2/3)
turtle.setup(850,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("green")
turtle.done()




