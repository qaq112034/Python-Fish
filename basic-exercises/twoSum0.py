nums = [2, 7, 11, 15]
target = 9

n = len(nums)# 获取 nums 的长度，并将结果存放到 n 变量中 #
for i in range(n):
    for j in range(n):#这里填的应该是(i+,n)#
        if nums[i] + nums[j] == target:
            print("[",i,",",j,"]")#直接print([i,j])#
            # 将找到的两个元素下标值以列表的形式打印出来 #




"""
while True:#定义一个元素为True，特定条件下此变量改为False来跳出循环#
    nums = []#在循环外定义#
    x = input("请录入一个整数（输入STOP结束）:")
    nums.append(x)
    if x == 'STOP':  #当X != STOP 时执行添加指令否者 前面定义的元素变为False跳出循环#
        break
target = input("请输入目标整数:")
#此处也是定义一个元素为False当此元素不满足条件是改为True，此题就是当不满足循环条件时元素改为True#
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print([i,j])
       #还要考虑列表是否存在两数相加等于目标数的情况#     
"""



###############
"""
nums = []

isInput = True
while isInput == True:
    x = input("请录入一个整数（输入STOP结束）：")
    if x != "STOP":
        nums.append(int(x))
    else:
        isInput = False

target = int(input("请录入目标整数："))

isFind = False
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
            isFind = True

if isFind == False:
    print("找不到！")
    """
    ###################




"""
import random
y = 0
while y <= 10000:
    nums = []
    x = random.randint(1,65535)
    nums.append(x)
    y += 1
target = input("请输入目标整数:")
for i in range(10000):
    for j in range(10000):
        if nums[i] + nums[j] == target:
            print("[",i,",",j,"]")


"""
