"""
fruits = ["苹果", "香蕉", "橘子"]
print(fruits[0])
print(fruits[1])
print(fruits[2])


my_list = ["Fish", 21, "南宁", True]
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])
print(len(my_list))
"""
"""
fruits = ["苹果", "香蕉", "橘子"]
fruits.append("葡萄")
print(fruits)
for fruit in fruits:
    print(f"我喜欢吃{fruit}")
person_list = ["Fish", 21, "南宁"]
for x in person_list:
    print(f"我的信息:{x}")
"""



"""
fruits = ["苹果", "香蕉", "橘子"]
print(fruits)
fruits.append("桃子")
print(fruits)
x = fruits[0]
fruits[0] = fruits[-1]
fruits[-1] = x
print(fruits)
"""

"""
person_list = ["Fish", 21, "南宁"]
print(person_list[0])

person_dict = {
    "name": "Fish",
    "age": 21,
    "city": "南宁"
    }
print(person_dict["name"])
print(person_dict["age"])
print(person_dict["city"])
student = {
    "name": "小明",
    "score": 95,
    "subjects": ["数学", "英语", "语文"]
    }
print(student["name"])
print(student["score"])
print(student["subjects"])
print(student["subjects"][0])
"""
"""
age = int(input("请输入你的年龄:"))

if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")
"""



def say_hello():
    print("你好!")
    print("欢迎来学Python!")

say_hello()


def add(a, b):
    result = a + b
    return result

sum_result = add(3, 5)
print(sum_result)


def introduce(name, age):
    print(f"我叫{name}, 今年{age}岁")
    
introduce("Fish", 21)


def add_three(x, y, z):
    result = x + y + z
    return result
sum = add_three(1, 2, 3)
print(sum)


