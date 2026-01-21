import math


def square(number):
    return math.ceil(number)


a = float(input("Введите длину стороны:"))
result = square(a*a)

print(f"Площадь квадрата = {result}")
