n = int(input("请输入一个正整数:"))
temp = n
res = []
i = 2
while i * i <= temp:
    while temp %i == 0:
        res.append(str(i))
        temp //= i
        i += 1
    if temp > 1:
        res.append(str(temp))
    print(f"{n} = {'x'.join(res)}")
