#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
##_*_ conding:UTF-8 _*_
#递归法

def f(n,a):
    if(n==1):
        return a
    else:
        r=f(n-1,a)*10+a
        return r

n=int(input("n="))
a=int(input("a="))
print("")
sum=0
for i in range(1,n+1):
    print(f(i,a))
    sum=sum+f(i,a)

print("sum=",sum)