first_num = int(input("Кубик Кости: "))
second_num = int(input("Кубик владельца: "))

if first_num >= second_num:
    print(f"Разность двух чисел {first_num - second_num}")
    print("Игрок платит")
else:
    print(f"Сумма: {first_num + second_num}")
    print("Владелец платит")
print("Игра окончена")