import unit

id = []
money_sum = []
times = []
money_aver = []
score = []
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
    money_aver.append(float(i[3]))
aver = float(data[0][4])/float(data[0][5])
# print(id)
# print(money_sum)
# print(times)
# print(money_aver)
# print(aver)
for i in range(len(id)):
    score.append(int(money_aver[i]*0.8+money_sum[i]*0.1+times[i]*0.1))
print(score)
for j in range(len(score)):
    score_sum = score_sum + int(score[i])
    money_sum_sum = money_sum_sum + int(money_sum[i])
    money_aver_sum = money_aver_sum + int(money_aver[i])
    times_sum = times_sum + int(times[i])
print(score_sum/len(score))
print(money_sum_sum/len(score))
print(money_aver_sum/len(score))
print(times_sum/len(score))
#202