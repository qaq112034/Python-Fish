x = input("请输入血液中的酒精含量:")
x = int(x)
if x < 20:
    print("不构成饮酒行为")
elif 20 <= x < 80:
    print("已经达到酒后驾驶的标准")
elif x >= 80:
    print("已经达到醉酒驾驶的标准")
else:
    print("请输入正确的酒精含量!")
