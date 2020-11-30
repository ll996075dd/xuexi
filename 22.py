#对10个数进行排序。
# -*- coding: UTF-8 -*-
n = 0
S = []
T = []
for num in range(1,11):
    a = int(input("输入: "))
    S.append(a)
for n in range(1,11):
    b = min(S)
    T.append(b)
    S.remove(b)#清空b中元素
print (T)
#3个函数，min,append,removed 
# 只可以针对数组元素