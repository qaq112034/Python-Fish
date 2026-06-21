while True:
    num1 = float(input("请输入第一个数:"))
    op = input("请输入运算符（+ - * /）:")
    num2 = float(input("请输入第二个数:"))

    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        res = num1 / num2
    else:
        print("运算符错误!")
        continue
    print(f"结果:{res}")

    again = input("是否继续计算?(y/n):").strip().lower
    if again != "y":
        print("退出计算器")
        break
