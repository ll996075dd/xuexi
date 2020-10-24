#_*_ conding:UTF-8 _*_
#题目：输出指定格式的日期。


from datetime import *
import time

#返回当前本地时间
print("today:"+str(date.today()))#datetime.date.today()默认
print("today:"+str(date.fromtimestamp(time.time())))#第2种方法，时间戳转换成字符串日期时间
