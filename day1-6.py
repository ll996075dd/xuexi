#_*_ conding:UTF-8 _*_
#题目：输入某年某月某日，判断这一天是这一年的第几天？

'''year = int(input('year:\n'))
month = int(input('mouth:\n'))
day = int(input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month <= 12:
    sum = months[month - 1]
else:
        print('输入错误')
sum += day
leap = 0 
if(year % 400 == 0) or ((year % 4 == 0)and (year % 100 != 0)):
    leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
        print('%d-%d-%d它是第%d天' %(year, month, day,sum))'''

#改
p = [31,28,31,30,31,30,31,31,30,31,30,31]
r = [31,29,31,30,31,30,31,31,30,31,30,31]
year = int(input('year:\n'))
month = int(input('mouth:\n'))
day = int(input('day:\n'))
if year % 400 == 0:
    time = p
else:
    time = r
if year % 4 == 0:
    time = p
else:
    time = r

days = sum(time[0:month-1])+day
print ('%d.%d.%d是%d年的第%s天。' %(year,month,day,year,days))


