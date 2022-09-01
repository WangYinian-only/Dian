from flask import Flask, render_template

import unit

app = Flask(__name__)

# sql = 'SELECT `用户编号`,`guiyi_money`,`guiyi_ci` FROM `居民客户的用电缴费习惯分析2` ORDER BY (`用户编号`);'
# sql = 'UPDATE `居民客户的用电缴费习惯分析2` SET guiyi_money = (( `缴费总额` - 254 )/ 1246 );'
# sql = 'UPDATE `居民客户的用电缴费习惯分析2` SET guiyi_ci = (( `缴费次数` - 3 )/ 5 );'
sql = 'SELECT * FROM `居民客户的用电缴费习惯分析2`;'
db = unit.MysqlHelper(database='dianshang', user='root', passwd='602511dtywyy', port=3306, host='localhost')
data = db.all(sql)
print(data)



