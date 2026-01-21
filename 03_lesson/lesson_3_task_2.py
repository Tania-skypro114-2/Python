from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "Galaxy", "+79231112233"),
    Smartphone("Iphone", "Iphone15", "+79234445566"),
    Smartphone("Redmi", "9A", "+79237778899"),
    Smartphone("Lenovo", "K5 Pro", "+79231234152"),
    Smartphone("Xiaomi", "16Pro max", "+79232506341"),
  ]


for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.mod}.{smartphone.num}")
