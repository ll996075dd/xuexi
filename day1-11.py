#_*_ conding:UTF-8 _*_
#题目：暂停一秒输出。
import time

l=[1,2,3,4]
for i in range(len(l)):
    print (l[i])
    time.sleep(1)  # 暂停一秒输出,进行缓冲 time.sleep函数