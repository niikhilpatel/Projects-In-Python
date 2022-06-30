import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
Symbols = "[]{}()*;/,_-"
all = lower + upper + numbers + Symbols
length = 16
password = ''''.join(random.sample(all,length))
print(password)