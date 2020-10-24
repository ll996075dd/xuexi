# _*_ conding: UTF-8_*_
#第一种
def fib(n):#定义一个函数
    a,b = 1,1
    for i in range(n-1):
        a, b = b,a + b
    return a
print (fib(10))
#第二种
# 使用递归
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
 
# 输出了第10个斐波那契数列
print (fib(10))
#第三种
def fbn(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
 
# 输出前 10 个斐波那契数列
print (fbn(10))