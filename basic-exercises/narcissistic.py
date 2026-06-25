"""
for i in range(100,1000):# 请在此处填写一个正确的循环语句 #:
    sum = 0
    temp = i
    
    while True: # 请在此处填写一个正确的循环语句 #:
        sum = sum + (temp % 10) ** 3
        temp //= 10
    
    if sum == i:
        print(i)
        """
for i in range(100,1000):
    if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 100 % 10) ** 3 ==i:
        print(i)
