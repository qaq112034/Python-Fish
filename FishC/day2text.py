x = input("请输入你的分数：")
while x != 'e':
    x = int(x)
    if x < 60:
        print("D")
    if 60 <= x < 80:
        print("C")
    if 80 <= x < 90:
        print("B")
    if 90 <= x < 100:
        print("A")
    if x == 100:
        print("S")
    x = input("请输入你的分数：")
