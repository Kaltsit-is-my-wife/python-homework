#例4.3
import json
import pygal

f = open("vix_daily.json", 'r')
vix_values = json.load(f)

dates, close = [], []
for i in range(len(vix_values)):
    if not i % 5:
        dates.append(vix_values[i]['Date'])
        close.append(vix_values[i]['VIX Close'])

bar = pygal.Bar(x_label_rotation=45, show_minor_x_labels=False, show_legend=False)
bar.x_labels = dates
bar.x_labels_major = dates[::26]
bar.add("Close", close)
bar.title = "CBOE Volatility Index (VIX)"
bar.x_title = "Date"
bar.y_title = "Close"
bar.render_to_file("vix_daily.svg")
print("Please check file: vix_daily.svg.")

#1
postal_code = input("请输入邮政编码:")
province_code = {
    '11': '北京市', '12': '天津市', '13': '河北省', '14': '山西省', '15': '内蒙古自治区',
    '21': '辽宁省', '22': '吉林省', '23': '黑龙江省', '31': '上海市', '32': '江苏省',
    '33': '浙江省', '34': '安徽省', '35': '福建省', '36': '江西省', '37': '山东省',
    '41': '河南省', '42': '湖北省', '43': '湖南省', '44': '广东省', '45': '广西壮族自治区',
    '46': '海南省', '50': '重庆市', '51': '四川省', '52': '贵州省', '53': '云南省',
    '54': '西藏自治区', '61': '陕西省', '62': '甘肃省', '63': '青海省', '64': '宁夏回族自治区',
    '65': '新疆维吾尔自治区', '71': '台湾省', '81': '香港特别行政区', '82': '澳门特别行政区'
}
if len(postal_code) == 6 and postal_code.isdigit():
    prefix = postal_code[:2]
    print(province_code.get(prefix, "未知省份"))
else:
    print("无效的邮政编码")

#2
n = int(input("请输入n:"))
text = input("请输入文本:")
for _ in range(n):
    print(text)

#3
import json
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read().lower()
char_counts = {}
for char in content:
    char_counts[char] = char_counts.get(char, 0) + 1
with open("char_stat.json", "w", encoding="utf-8") as f:
    json.dump(char_counts, f, ensure_ascii=False)

#4
pi_accu = {}
n = 10
for i in range(1, n + 1):
    item = (-1) ** (i + 1) / (2 * i - 1)
    if i == 1:
        accu = item
    else:
        accu += item
    if i % 2 == 0:
        pi_accu[i] = {"item": item, "pi": 4 * accu, "accu": accu}

#5
import tkinter as tk
from tkinter import filedialog
import pygal
import re
from collections import Counter

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")])

if file_path:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    top_words = Counter(words).most_common(50)
    words, counts = zip(*top_words) if top_words else ([], [])

    bar = pygal.Bar(x_label_rotation=45, show_legend=False)
    bar.title = 'Top 50 Word Frequencies'
    bar.x_labels = words
    bar.add('Frequency', counts)
    bar.render_to_file('word_freq.svg')

root.destroy()

#6
import pygal
import random

expected = {2:1/36, 3:2/36, 4:3/36, 5:4/36, 6:5/36, 7:6/36,
            8:5/36, 9:4/36, 10:3/36, 11:2/36, 12:1/36}
counts = {i:0 for i in range(2, 13)}

for _ in range(1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    counts[total] += 1

frequencies = {k: v/1000 for k, v in counts.items()}

line_chart = pygal.Line()
line_chart.title = 'Dice Roll Frequency vs Expected'
line_chart.x_labels = list(range(2, 13))
line_chart.add('Actual', [frequencies[i] for i in range(2, 13)])
line_chart.add('Expected', [expected[i] for i in range(2, 13)])
line_chart.render_to_file('dice_frequency.svg')