#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
## -*- coding: UTF-8 -*-

def output(s,l):#从第一个数字筛选，将最后一个数字筛选出来
    if l == 0:
        return
    print (s[l-1])
    output(s,l-1)
s = input("请输入5个数:")
l = len(s)
output(s,l)
#核心代码
# if l == 0:
# return
# print (s[l-1])