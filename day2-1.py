#_*_ conding:UTF-8 _*_
#题目：暂停一秒输出，并格式化当前时间。
import time

print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#晚一秒输出
time.sleep(1)
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))