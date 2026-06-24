import random

x = random.sample(range(1,34),k=6)
y = random.sample(range(1,17),k=1)
print("开奖结果是：",*x)
print("特别号码是：", *y)
