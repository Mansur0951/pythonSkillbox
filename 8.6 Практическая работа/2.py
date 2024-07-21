dept_count = int(input("Введите количество должников: "))
all_debt = 0

for i in range(0, dept_count+1, 5):
    print(f"Должник с номером {i}")
    owe_sum = int(input("Сколько должны? "))
    all_debt += owe_sum

print(f"\nОбщая сумма долга: {all_debt}")