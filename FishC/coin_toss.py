import random

counts = int(input("请输入抛硬币的次数："))
i = 0
x = 0
y = 0
a = 0
b = 0
print("开始抛硬币实验......")
if counts < 100:
    
    while i < counts:
        num = random.randint(1, 10)

        if num % 2:
            print("正面",end=" ")
            x += 1
        else:
            print("反面",end=" ")
            y += 1
        i += 1
else:
    while i < counts:
        num = random.randint(1, 10)

        if num % 2:
            x += 1
        else:
            y += 1
        i += 1
print("一共模拟了",counts,"次抛硬币，结果如下:")
print("正面:",x,"次" ,"\n""反面:",y,"次",)
print(num)
