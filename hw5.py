#2.2
from math import radians, sin, cos, acos

# 输入两点的纬度和经度（度），并转换为弧度
t1 = radians(float(input("Latitude of the first point (in degrees): ")))
g1 = radians(float(input("Longitude of the first point (in degrees): ")))
t2 = radians(float(input("Latitude of the second point (in degrees): ")))
g2 = radians(float(input("Longitude of the second point (in degrees): ")))

# 应用球面余弦定理计算距离（地球半径6371.01千米）
distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

# 输出结果，保留1位小数
print("The distance between the two points on the earth is:", round(distance, 1), "km.")


#2.3
import numpy_financial as npf

# 输入贷款参数
principal = int(input("Loan principal: "))  # 贷款本金
nper = int(input("Number of periods: "))  # 还款期数
rate = float(input("Interest rate (decimal): "))  # 每期利率（小数形式）

# 计算每期付款额（pmt函数：rate=利率，nper=期数，pv=-本金）
payment = npf.pmt(rate, nper, -principal)

# 输出表头
print("Period\tPayment\tPrincipal Paid\tInterest Paid\tPrincipal Left")

# 循环计算每期还款明细
remaining_principal = principal
for period in range(1, nper + 1):
    interest_paid = remaining_principal * rate  # 本期利息
    principal_paid = payment - interest_paid  # 本期本金
    remaining_principal -= principal_paid  # 剩余本金

    # 格式化输出（保留2位小数，制表符分隔对齐）
    print(f"{period}\t{payment:.2f}\t{principal_paid:.2f}\t{interest_paid:.2f}\t{remaining_principal:.2f}")

#题一
n = int(input("请输入项数: "))
def fibonacci(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print(fibonacci(n))

#题二
import time

n = int(input("请输入项数: "))
start_time = time.time()

def calculate_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) * 4 / (2 * i + 1)
    return pi

result = calculate_pi(n)
end_time = time.time()

print("圆周率计算结果:", result)
print("程序运行耗时:", end_time - start_time, "秒")

#题三
pv = float(input("请输入贷款总额: "))
rate = float(input("请输入利率（年利率除以12）: "))
nper = int(input("请输入还款期数: "))

def calculate_payment(pv, rate, nper):
    return pv * rate * (1 + rate) ** nper / ((1 + rate) ** nper - 1)

payment = calculate_payment(pv, rate, nper)
print("每期付款金额:", payment)

#案例
from decimal import Decimal
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt

pi = 3
a, b, c = 2, 3, 4
item_values = []
pi_values = []
accu_values = []

for i in range(2, 300000):
    if not i % 2:
        pi += Decimal(4 / (a * b * c))
    else:
        pi -= Decimal(4 / (a * b * c))
    item_values.append(i)
    pi_values.append(pi)
    a, b, c = a + 2, b + 2, c + 2

file_name = askopenfilename()
pi_file = open(file_name, 'r')
pi_text = pi_file.read()
pi_file.close()

pi_text = pi_text.replace(' ', '')
pi_text = ''.join(pi_text.split('\n'))
pi_text = pi_text[2:]

for pi in pi_values:
    pi_str = str(pi)
    pi_str = pi_str[2:]
    for i in range(len(pi_str)):
        if pi_str[i] != pi_text[i]:
            break
    accu_values.append(i)

plt.plot(item_values, accu_values, linewidth=5)
plt.title("Computing Pi with Infinite Series", fontsize=16)
plt.xlabel("Number of items", fontsize=12)
plt.ylabel("Number of accurate decimal places", fontsize=12)
plt.tick_params(axis='both', labelsize=12)
plt.show()