#题目：按逗号分隔列表。
#-*- coding: UTF-8 -*-
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print (s1)
#在每个数后面加入，