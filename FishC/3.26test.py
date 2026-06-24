'''
i = 2
while i < 10:
    x = 2
    while x < i:
        if i % x == 0:
            print(i, "=",x,"*", i //x,)
            break
        x += 1
    else:
        print(i,"是一个素数",)
    i += 1
''' #while循环找出10以内的所有素数
for i in range(2,11):
    for x in range(2,i):
        if i % x ==0:
            print(i,"=",x,"*", i // x)
            break
        x += 1
    else:
        print(i,"是一个素数",)
        i += 1
