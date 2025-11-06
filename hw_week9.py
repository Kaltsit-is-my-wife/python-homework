import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from tkinter import filedialog
import json
import pygal
from string import punctuation


def save_user_input():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.asksaveasfilename(title="另存为",
                                            defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filename:
        print("已取消。")
        return
    exists = os.path.exists(filename)
    print("请输入要保存的内容（单独一行输入英文句号 . 结束，或按 Ctrl+D/Ctrl+Z+Enter 结束）:")
    lines = []
    try:
        while True:
            line = input()
            if line == '.':
                break
            lines.append(line)
    except EOFError:
        pass
    mode = 'a' if exists else 'w'
    with open(filename, mode, encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

    print(f"{'追加到' if exists else '已创建并保存到'}: {filename}")

def future_values(P, r, c, n):
    vals = [P]  # 年 0 的终值（初始本金）
    for _ in range(n):
        vals.append(vals[-1] * (1 + r) + c)
    return vals  # 返回长度为 n+1 的列表，对应 0..n 年

def caculate():
    try:
        P = float(input("初始本金 P (例如 1000): ") or 1000)
        r = float(input("年利率（%） (例如 5): ") or 5) / 100.0
        c = float(input("每年追加金额 c (例如 100): ") or 100)
        n = int(input("年份数 n (例如 10): ") or 10)
    except Exception as e:
        print("输入错误:", e)
        return

    vals = future_values(P, r, c, n)
    years = list(range(0, n + 1))

    plt.figure(figsize=(8, 4.5))
    plt.plot(years, vals, marker='o', linewidth=2)
    plt.title("计算终值（折线图）")
    plt.xlabel("年")
    plt.ylabel("终值")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(years)
    plt.tight_layout()

    out = "future_value.png"
    plt.savefig(out)
    plt.show()

def gdpGenerator():
    file_name = askopenfilename(filetype=[('JSON files', '*.json')])
    f = open(file_name, 'r')
    values = json.load(f)
    f.close()

    CHN, USA, GBR, IND = {}, {}, {}, {}
    for each in values:
        if each['Country Code'] == 'CHN':
            CHN[each['Year']] = each['Value']
            continue
        if each['Country Code'] == 'USA':
            USA[each['Year']] = each['Value']
            continue
        if each['Country Code'] == 'GBR':
            GBR[each['Year']] = each['Value']
            continue
        if each['Country Code'] == 'IND':
            IND[each['Year']] = each['Value']

    line = pygal.Line(x_label_rotation=-45, show_minor_x_labels=False)
    line.x_labels = list(CHN.keys())
    line.x_labels_major = list(CHN.keys())[::2]
    line.add("China", list(CHN.values()))
    line.add("United States", list(USA.values()))
    line.add("United Kingdom", list(GBR.values()))
    line.add("India", list(IND.values()))
    line.x_title = "Year"
    line.y_title = file_name.split('/')[-1].split('.')[-1].capitalize()
    line.render_to_file(file_name.split('/')[-1].split('.')[0] + '_compared.svg')
    print("Please check file: %s_compared.svg." % file_name.split('/')[-1].split('.')[0])

def words():
    file_name = input("File to analyze: ")
    f = open(file_name, 'r')
    text = f.read()
    f.close()

    text = text.lower()
    for ch in punctuation:
        if ch != "'":
            text = text.replace(ch, '')
    words = text.split()

    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    freq = list(zip(counts.values(), counts.keys()))
    freq.sort(reverse=True)

    n = int(input("Output analysis of how many words? "))
    for i in range(n):
        print("%5d: %-15s" % freq[i])

if __name__ == "__main__":
    words()