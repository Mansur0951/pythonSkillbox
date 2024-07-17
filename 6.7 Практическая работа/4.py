rate_count = int(input("How much we rate app? "))
pl_num = 0
min_num = 0

while rate_count != 0:
    rate = int(input("Введите число: "))
    rate_count -= 1
    if rate >= 0:
        pl_num += 1
    else:
        min_num += 1

print("Кол-во положительных чисел:", pl_num)
print("Кол-во отрицательных  чисел:", min_num)
