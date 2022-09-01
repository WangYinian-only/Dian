from flask import Flask, render_template

import unit

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/zhuzhuangtu')
def echarts():
    sql = 'select * from 居民客户的用电缴费习惯分析2'
    db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
    data = db.all(sql)
    print(data)
    return render_template("zhuzhuangtu.html", data=data)


@app.route('/zhexiantu')
def echarts4():
    data1 = []
    data2 = []
    data3 = []
    sql = 'select * from 居民客户的用电缴费习惯分析2'
    db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
    data = db.all(sql)
    for i in data:
        data1.append('用户' + str(int(i[0]) - 1000000000))
        data2.append(int(i[1]))
        data3.append(int(i[2]))
    print(data)
    print(data2)
    print(data3)
    return render_template("zhexiantu.html", data1=data1, data2=data2, data3=data3)


@app.route('/tubiaoliandong')
def echarts5():
    data1 = []
    data2 = []
    sql = 'select 用户类型,count(*) from 居民客户的用电缴费习惯分析2 group by 用户类型'
    db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
    data = db.all(sql)
    for i in data:
        data1.append(i[0])
        data2.append(i[1])
    print(data)
    return render_template("1.html", data=data, data1=data1, data2=data2)


@app.route('/top5')
def echarts6():
    id = []
    money_sum = []
    times = []
    money_aver = []
    score = []
    average = []
    score_sum = 0
    money_sum_sum = 0
    money_aver_sum = 0
    times_sum = 0
    sql = 'select * from 居民客户的用电缴费习惯分析2 where 用户类型 = "高价值型客户"'
    db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
    data = db.all(sql)
    for i in data:
        id.append(i[0])
        money_sum.append(int(i[1]))
        times.append(int(i[2]))
        money_aver.append(float(i[1]) / float(i[2]))
    # print(id)
    # print(money_sum)
    # print(times)
    # print(money_aver)
    # print(aver)
    for i in range(len(id)):
        score.append(int(money_aver[i] * 0.2 + money_sum[i] * 0.5 + times[i] * 0.3))
    print(score)
    for j in range(len(score)):
        score_sum = score_sum + int(score[i])
        money_sum_sum = money_sum_sum + int(money_sum[i])
        money_aver_sum = money_aver_sum + int(money_aver[i])
        times_sum = times_sum + int(times[i])
    a = score_sum / len(score)
    b = money_sum_sum / len(score)
    c = money_aver_sum / len(score)
    d = times_sum / len(score)
    average.append(a)
    average.append(b)
    average.append(c)
    average.append(d)
    data1 = []
    data2 = []
    data3 = []
    sql = 'select * from 居民客户的用电缴费习惯分析2'
    db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
    data = db.all(sql)
    for i in data:
        if i[0] in ["1000000099", "1000000098", "1000000019", "1000000046", "1000000066"]:
            data1.append(i)

    for i in data:
        if i[0] in ["1000000099", "1000000098", "1000000019", "1000000046", "1000000066"]:
            data2.append(float(i[1]) / float(i[2]))

    print(data1)
    return render_template("2.html", data=data1, data2=data2)


# 1000000099
# 1000000098
# 1000000019
# 1000000046
# 1000000066


if __name__ == '__main__':
    app.run()
