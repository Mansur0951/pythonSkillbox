experiense = int(input("Введите количество опыта: "))

if experiense >=  1000 and experiense < 2500:
    print("Ваш уровень: 2")
elif experiense >= 2500 and experiense < 5000:
    print("Ваш уровень: 3")
elif experiense >= 5000:
    print("Ваш уровень: 6")
else:
    print("error")