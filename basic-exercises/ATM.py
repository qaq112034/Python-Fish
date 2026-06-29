money = 1000
while True:
    print("\n1查询余额 2取款 3存款 4退出")
    op = input("操作: ")
    if op == "1":
        print(f"当前余额:{money}元")
    elif op == "2":
        get = int(input("取款金额: "))
        if get > money:
            print("余额不足")
        else:
            money -= get
            print("取款成功")
    elif op == "3":
        add = int(input("存款金额: "))
        money += add
        print("存款成功")
    elif op == "4":
        break
