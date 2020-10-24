#_*_ conding:UTF-8 _*_
#题目：判断1-200之间有多少个素数，并输出所有素数。
#满足素数条件，只能被自身和1整除的数
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(1,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i ==0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' %m )
        h +=1
        if h % 10 == 0:
            print ("")
    leap =1
print('素数是%d' %h )