#第二章
#案例：蒙特卡洛模拟
import random
n = int(input("请输入模拟的点数: "))
count = 0
for i in range(n):
    x = random.random() * 2 - 1           #等价于x=random.uniform(-1, 1)
    y = random.random() * 2 - 1
    distance_squared = x ** 2 + y ** 2
    if distance_squared <= 1:
        count += 1

pi = 4 * count / n
print(f"通过蒙特卡洛模拟计算得到的圆周率π值为: {pi}")

#例题
#2.1
pi = 3
a, b, c = 2, 3, 4
for i in range(2, 9999):
    if not i % 2:
        pi += 4 / (a * b * c)
    else:
        pi -= 4 / (a * b * c)
    print(f"{i:02d} items: pi = {pi:9.7f}")
    a, b, c = a + 2, b + 2, c + 2

#2.2
from math import radians, sin, cos, acos

t1 = radians(float(input("Latitude of the first point (in degrees): ")))
g1 = radians(float(input("Longitude of the first point (in degrees): ")))
t2 = radians(float(input("Latitude of the second point (in degrees): ")))
g2 = radians(float(input("Longitude of the second point (in degrees): ")))
d = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print("The distance between the two points on the earth is: ", round(d, 1), "km.")


#2.3
from random import random
n = int(input("How many steps do you intend to take through the simulation? "))

steps = 0
for i in range(n):
    x = 2 * random() - 1
    if x > 0:
        steps += 1
    else:
        steps -= 1
print(f"The object has traveled {steps} steps based on the simulation.")

#2.4
from math import sin, cos, radians
from random import random
n = int(input("How many steps do you intend to take through the simulation? "))
x, y = 0, 0
for i in range(n):
    angle = 360 * random()
    x += cos(radians(angle))
    y += sin(radians(angle))

print(f"The object has traveled to ({x:5.1f},{y:5.1f}) after {n} steps based on the simulation.")


#第二章课后题
#1.计算
import math

# 读取用户输入的两个整数
a = int(input("请输入整数 a: "))
b = int(input("请输入整数 b: "))

# +-*
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
# ÷ 与 取余
if b != 0:
    print(f"a / b: {a / b}")
    print(f"a // b: {a // b}")
    print(f"a % b: {a % b}")
else:
    print("a / b: 除数不能为 0")
    print("a // b: 除数不能为 0")
    print("a % b: 除数不能为 0")
# log
if a > 0:
    print(f"log₁₀a: {math.log10(a)}")
else:
    print("log₁₀a: 真数必须大于 0")
# 幂
if a == 0 and b == 0:
    print("a^b: 数学上无意义")
elif a == 0:
    print("a^b: 0")
else:
    print(f"a^b: {pow(a, b)}")

#2.球
import math

r = float(input("请输入球体的半径 r: "))
S = 4 * math.pi * (r ** 2)
V = (4.0 / 3.0) * math.pi * (r ** 3)
print(f"球体的表面积为: {S:.2f}")
print(f"球体的体积为: {V:.2f}")

#3.面积
import math

s1 = float(input("请输入三角形的第一条边长 s1: "))
s2 = float(input("请输入三角形的第二条边长 s2: "))
s3 = float(input("请输入三角形的第三条边长 s3: "))

s = (s1 + s2 + s3) / 2.0
area = math.sqrt(max(s * (s - s1) * (s - s2) * (s - s3), 0.0))
print(f"三角形的面积为: {area:.2f}")

#4.随机数排序
import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

nums = [num1, num2, num3]
sorted_nums = sorted(nums)

print("1-100中随机生成的三个数从小到大依次为：")
print(sorted_nums[0], sorted_nums[1], sorted_nums[2])

#5.平均数
n = int(input("请输入要计算的数字个数: "))
values = []
for i in range(1, n + 1):
    values.append(float(input(f"请输入第 {i} 个数字: ")))
average = sum(values) / n if n > 0 else float("nan")
print(f"这些数字的平均数是: {average}")