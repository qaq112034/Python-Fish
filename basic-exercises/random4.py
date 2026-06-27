import random
import string
code = "".join(random.choices(string.ascil_uppercase + string.digits, k = 4))
print("本次验证码:", code)
