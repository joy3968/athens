# # 암호화
#
import bcrypt

password = 'pass1234'
b = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#
# print(b)


import random
import string


random_code =''
string_code = string.ascii_letters + string.digits

for i in range(6):
    random_code += random.choice(string_code)

print(random_code)


