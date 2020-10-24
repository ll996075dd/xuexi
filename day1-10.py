#_*_ conding:UTF-8 _*_
#题目：输出 9*9 乘法口诀表。
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')#end=' '意思是末尾不换行，加空格
    print()