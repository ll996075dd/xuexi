'''给一个不多于5位的正整数，
要求：一、求它是几位数，二、逆序打印出各位数字。
程序分析：学会分解出每一位数。'''

def output(num,l):
    if l == 0:
        return
    print (num[l-1])
    output(num,l-1)
num = input("请输入一个不多于5位的正整数:")
l = len(num)
output(num,l)
print('\n长度是为%d' %l)
#递归调用
