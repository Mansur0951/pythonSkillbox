enter_num = int(input("Введите число: "))
fact_sum = 1

for i in range(1, enter_num+1):
    fact_sum *= i

print(f"Факториал числа {enter_num} равен {fact_sum}")