import string
s = input('请输入一个字符串:\n')
letters = 0
i =0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
print ('%d' %letters)