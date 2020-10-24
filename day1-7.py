#_*_ conding:UTF-8 _*_
#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
l = []
for i in range(3):#连续输入三个数
    x = int(input('请输入:\n'))
    l.append(x)
l.sort()#归纳函数，自动进行排列
print(l)