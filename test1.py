# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)  # 显示全部行
pd.set_option('display.max_columns', None)  # 显示全部列

# 读取文件
df = pd.read_excel("dian.xlsx", engine='openpyxl')

# 统计数量
long = len(df['缴费金额（元）'])
# df['平均缴费金额'] = df['缴费金额（元）']/long

# 每个用户的总金额
tjj = df.groupby(by='用户编号')['缴费金额（元）'].sum()
data = df.groupby(by='用户编号')['缴费金额（元）'].count()


# print(tjj)

# print(data)

# 统计次数
def tjc(data):
    num = 0
    for i in data:
        num += i
    # print(num / 100)
    return num/100


# 所有金额平均
def average(data):
    sum = 0
    for x in data:
        sum += x
    # print(sum / 100)
    return sum/100


# average(tjj)

# 输出表数据
# print(df)

# print(df.describe())  # 统计

df['平均次数'] = tjc(data)
df['平均金额'] = average(tjj)
print(df)

# df.to_csv('居民客户的用电缴费习惯分析 1.csv')