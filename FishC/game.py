""" 用Python设计第一个游戏 """
import random

counts = 10
answer = random.randint(1,10)

while counts > 0:
    temp = input("不妨猜一下小甲鱼心里想的是哪个数字:")
    guess = int(temp)

    if guess == answer:
            print("猜对了^_^")
            break
    else:
        if guess < answer:
            print("小了")
        else:
            print("大了")
        counts = counts - 1
        
print("游戏结束，不玩啦^_^")
