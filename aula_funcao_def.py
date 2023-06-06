import random

def soma(a, b ,c):
    print(f'{a=} + {b=} + {c=} = ', a + b + c)

num1 = random.randint(0, 500)
num2 = random.randint(0, 600)
num3 = random.randint(0, 700)

soma(num1, num2, num3)
soma(num1, num2, num3)
soma(b=num1, c=num2, a=num3)