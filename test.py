
import unit

id = []
money_sum = []
times = []
money_aver = []
score = []
sql = 'select * from 居民客户的用电缴费习惯分析2 where 用户类型 != "高价值型客户"'
db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
data = db.all(sql)
for i in data:
    id.append(i[0])
    money_sum.append(int(i[1]))
    times.append(int(i[2]))
    money_aver.append(float(i[3]))
aver = float(data[0][4])/float(data[0][5])
# print(id)
# print(money_sum)
# print(times)
# print(money_aver)
# print(aver)
for i in range(len(id)):
    score.append(int(money_aver[i]*0.8+money_sum[i]*0.1+times[i]*0.1))
print(score.index(199))
print(score.index(172))
print(score.index(170))
print(score.index(166))
print(score.index(163))
for j in range(len(score)):
    if score[j]>202:
        print(score[j])
score.sort(reverse=True)
print(score)
print(id[58])
print(id[57])
print(id[4])
print(id[23])
print(id[35])
