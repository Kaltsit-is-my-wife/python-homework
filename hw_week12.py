def max_init(*values, init=100):
    max_value = init
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

#例题6.2
import csv

def main():
    course()
    print("%d courses; %d credits; GPA is: %.2f" % gpa())

def course(file="credit_score.csv"):
    courses = []
    more = True  # 是否继续输入
    while more:
        credit = input("Credit: ")  # 输入课程学分
        score = input("Score: ")  # 输入课程成绩
        courses.append([credit, score])
        cont = input("More courses? (Y/N) ")
        if cont.upper() != 'Y':
            more = False  # 不再继续输入
    f = open(file, 'w', newline='')
    csvWriter = csv.writer(f)
    csvWriter.writerows(courses)
    f.close()

def gpa(file="credit_score.csv"):
    f = open(file, 'r')
    courses = list(csv.reader(f))
    f.close()
    totalCourses = 0  # 课程门数
    totalCredits = 0  # 总学分
    totalGradePoints = 0  # 总绩点
    for each in courses:
        credit = int(each[0])  # 获取课程学分
        score = int(each[1])  # 获取课程成绩
        if score >= 95:
            gradePoint = 4.5
        elif score > 90:
            gradePoint = 4.0
        elif score >= 80:
            gradePoint = 3.5
        elif score >= 75:
            gradePoint = 3.0
        elif score >= 70:
            gradePoint = 2.5
        elif score >= 65:
            gradePoint = 2.0
        elif score >= 60:
            gradePoint = 1.0
        else:
            gradePoint = 0
        totalCourses += 1
        totalCredits += credit
        totalGradePoints += credit * gradePoint
    return (totalCourses, totalCredits, totalGradePoints / totalCredits)

#例题6.3
"""This module has two functions: fit_val() and max_init()."""

def fit_val(principal, year, rate=0.02):
    """Computing future value"""
    future_value = principal
    for i in range(year):
        future_value = future_value * (1+rate)
    return future_value

def max_init(*values, init=100):
    """Finding max value"""
    max_value = init
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

#题3
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = int(input("请输入第一个正整数："))
    num2 = int(input("请输入第二个正整数："))
    result = gcd(num1, num2)
    print(f"这两个数的最大公约数是：{result}")

#题4
def find_narcissistic_num(digits):
    if not (3 <= digits <= 8):
        print("位数必须在3~8之间！")
        return []

    start = 10 ** (digits - 1)
    end = 10 ** digits - 1
    narcissistic_nums = []
    for num in range(start, end + 1):
        total = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp = temp // 10

        if total == num:
            narcissistic_nums.append(num)
    return narcissistic_nums

if __name__ == "__main__":
    n = int(input("请输入位数（3~8）："))
    nums = find_narcissistic_num(n)
    if nums:
        print(f"{n}位的水仙花数有：{nums}")
