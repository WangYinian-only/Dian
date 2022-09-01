# -*- codeing = utf-8 -*-
# @Time : 2022/3/29 10:27
# @Author : 王伊念
# File : test2.py
# @Software : PyCharm
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)  # 显示全部行
pd.set_option('display.max_columns', None)  # 显示全部列

# 读取文件
df = pd.read_excel("dian.xlsx", engine='openpyxl')
tjj = df.groupby(by='用户编号')['缴费金额（元）'].sum().tolist()
data = df.groupby(by='用户编号')['缴费金额（元）'].count().tolist()
uid = df.groupby('用户编号').count().index

# print(uid)

sumj = 0
for i in tjj:
    sumj += i
avgj = sumj / 100

sumc = 0
for i in data:
    sumc += i
avgc = sumc / 100

Ut = []
for i in range(100):
    if tjj[i] < avgj and data[i] < avgc:
        Ut.append("低价值型客户")
    elif tjj[i] > avgj and data[i] < avgc:
        Ut.append("潜力型客户")
    elif tjj[i] > avgj and data[i] > avgc:
        Ut.append("高价值型客户")
    elif tjj[i] < avgj and data[i] > avgc:
        Ut.append("大众型客户")

Types = list(Ut)
rows = []
for i in range(100):
    # 创建一个新的字典
    newdata = dict(用户编号=uid[i], 缴费总额=tjj[i], 缴费次数=data[i], 用户类型=Types[i], 平均金额=avgj, 平均缴费次=avgc)
    rows.append(newdata)
df2 = pd.DataFrame(rows)
print(df2)
df2.to_csv('居民客户的用电缴费习惯分析 2.csv',index=False)
