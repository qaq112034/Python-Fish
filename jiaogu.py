n = int(input("请输入一个正整数："))
while n > 0:
    if n % 2 == 0:
        print(n,"/2","=",int(n/2),end='\n')
        n = int(n/2)
    else:
        print(n,"*3","+1","=",int(n*3+1),end='\n')
        n = int(n*3+1)
    if n == 1:
        break

