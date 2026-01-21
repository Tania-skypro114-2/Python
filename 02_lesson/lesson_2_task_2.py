def is_year_leap(number):
    return "True" if (number % 4 == 0) else "False"


year = int(input("Введите год:"))

result = is_year_leap(year)

print(f"год {year}: {result}")
