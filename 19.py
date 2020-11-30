#题目：练习函数调用。
# -*- coding: UTF-8 -*-
 
def hello_runoob():
    print ('RUNOOB')
 
def hello_runoobs():
    for i in range(0,3):
        hello_runoob()
if __name__ == '__main__':
    hello_runoobs()