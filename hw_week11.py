#5.5
import csv

courses = []
more = True  # 是否继续输入
while more:
    credit = input("Credit: ")  # 输入课程学分
    score = input("Score: ")  # 输入课程成绩
    course = (credit, score)
    courses.append(course)
    cont = input("More courses? (Y/N) ")
    if cont.upper() == 'N':
        more = False  # 不再继续输入

f = open("credit_score.csv", 'a', newline="")
csvWriter = csv.writer(f)
csvWriter.writerows(courses)
f.close()

#5.6
import csv

f = open("credit_score.csv",'r')
courses = list(csv.reader(f))
f.close()

totalCourses = 0  # 课程门数
totalCredits = 0  # 总学分数
totalGradePoints = 0  # 总绩点
for each in courses:
    credit = int(each[0])  # 获取课程学分
    score = int(each[1])  # 获取课程成绩
    if score >= 95: gradePoint = 4.5
    elif score >= 90: gradePoint = 4.0
    elif score >= 85: gradePoint = 3.5
    elif score >= 80: gradePoint = 3.0
    elif score >= 75: gradePoint = 2.5
    elif score >= 70: gradePoint = 2.0
    elif score >= 65: gradePoint = 1.5
    elif score >= 60: gradePoint = 1.0
    else: gradePoint = 0
    totalCourses += 1
    totalCredits += credit
    totalGradePoints += credit*gradePoint

print("%d courses; %d credits; GPA is %.2f." %
      (totalCourses,totalCredits,totalGradePoints/totalCredits))

#题1
weight = float(input("请输入体重(kg)："))
height = float(input("请输入身高(m)："))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 24:
    print("正常")
elif 24 <= bmi < 28:
    print("过重")
else:
    print("肥胖")
print(f"BMI值为：{bmi:.2f}")

#题2
while True:
    try:
        year = int(input("请输入年份："))
        zodiacs = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
        index = (year - 1996) % 12
        print(f"{year}年的生肖是{zodiacs[index]}")
        break
    except ValueError:
        print("输入错误，请输入整数年份")

#题3
try:
    n = int(input("请输入正整数n："))
    m = int(input("请输入正整数m："))
    while m != 0:
        n, m = m, n % m
    print(f"最大公约数是{n}")
except ValueError:
    print("输入错误")

#题4
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    if num == hundreds**3 + tens**3 + units**3:
        print(num)

#题5
import random

secret_num = random.randint(0, 1000)
while True:
    guess = int(input("请猜一个0到1000之间的整数："))
    if guess == secret_num:
        print("恭喜你，猜对了！")
        break
    elif guess > secret_num:
        print("太大")
    else:
        print("太小")

#题6
import csv

with open("multiplication_table.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for i in range(1, 10):
        row = []
        for j in range(1, i+1):
            row.append(f"{j}×{i}={i*j}")
            print(f"{j}×{i}={i*j}", end="\t")
        writer.writerow(row)
        print()

