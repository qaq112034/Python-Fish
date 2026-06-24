# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-150254-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) 2020 fishc.com.cn All rights reserved

steps = 7
i = 1
FIND = False

while i < 100:
    if i % 7 == 0:
        FIND = True
        break
    else:
        steps % 2 == 1
        steps % 3 == 2
        steps % 5 == 4
        steps % 6 == 5
        steps % 7 == 0
    i = i + 1

if FIND == True:
    print('阶梯数是：', steps)
else:
    print('在程序限定的范围内找不到答案！')
