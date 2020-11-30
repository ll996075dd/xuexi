#题目：求100之内的素数。
#-*- coding: UTF-8 -*-
for i in range(2,100):
    if 0  not in [i%n for n in range(2,i)]:
        print (i)