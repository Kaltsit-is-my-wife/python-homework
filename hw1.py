#1.1
str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")
result = str1 + str2
print("组合后的字符串是：", result)

#1.2
N = int(input("请输入一个正整数N："))
sum_result = sum(range(1, N + 1))
print("从1到",N,"的和为：", sum_result)

#1.3
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()

#1.4
import math

factorial_sum = sum(math.factorial(i) for i in range(1, 11))
print(factorial_sum)

#1.5
peaches = 1
for day in range(4, 0, -1):
    peaches = (peaches + 1) * 2
print("第一天共摘了桃子：", peaches)

#1.6
import itertools

ingredients = ["鸡肉", "鱼", "牛肉",  "蔬菜", "米饭"]
combinations = list(itertools.combinations(ingredients, 2))#combinations生成组合
print("组合形式：")
for combo in combinations:
    print(combo)

#1.7
import turtle

turtle.color("red")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()
turtle.done()

#1.8
import turtle#重复导入，但是鉴于是独立题目，保留了

turtle.speed(10)
for i in range(36):
    turtle.circle(100)
    turtle.right(10)
turtle.done()

#微实例
#1.1
radius = float(input("请输入圆的半径："))
area = 3.14159 * radius ** 2  # 使用圆周率的近似值
print("圆的面积是：", area)

#1.2
name = input("请输入你的名字：")
print("你好，" + name + "！很高兴认识你！")

#1.3
n = int(input("请输入要计算的斐波那契数列的项数："))
a, b = 0, 1
print("斐波那契数列的前", n, "项为：")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # 更新a和b的值
print()

#1.4
radius = float(input("请输入圆的半径："))
print("绘制一个半径为", radius, "的圆。")
print("圆的周长为：", 2 * 3.14159 * radius)
print("圆的面积为：", 3.14159 * radius ** 2)

#1.5
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("当前的日期和时间是：", current_time)

#1.6
rows = int(input("请输入矩形的行数："))
cols = int(input("请输入矩形的列数："))

print("输出的矩形为：")
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()  # 换行