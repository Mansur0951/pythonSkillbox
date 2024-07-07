first_chair = int(input("Цена 1 стула; "))
second_chair = int(input("Цена 2 стула; "))
third_chair = int(input("Цена 3 стула; "))
budget = 10000
check_sum = first_chair + second_chair + third_chair

if check_sum > budget:
    check_sum = (check_sum // 100) * 10

print(f"Сумма скидки {check_sum}")