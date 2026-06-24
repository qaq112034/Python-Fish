import random

while True:
    answer = random.randint(1,100)
    counts = 10
    print("=====游戏开始，你有10次机会=====")

    while counts > 0:
        temp = input("猜一猜我心里想的是哪个数吧:")
        guess = int(temp)

        if guess == answer:
            print("恭喜你，猜对了！")
            break
        else:
            if guess < answer:
                print("小了")
            else:
                print("大了")
            counts = counts - 1
            print(f"剩余次数:{counts}")

            
    if counts == 0:
        print(f"游戏结束！正确答案是：{answer}")

        
    while True:
        choice = input("是否再来一局？(y/n):").strip().lower()
        if choice in ["y","n"]:
            break
        print("请输入 y 或 n !")

        
    if choice == "n":
        print("游戏结束，再见！")
        break
