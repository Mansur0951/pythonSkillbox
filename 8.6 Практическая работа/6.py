educational_grant = 10000
expenses = 12000
needs = 0

for i in range(1, 11):
    if i == 1:
        needs += expenses - educational_grant
        print(f"{i}. месяц траты {expenses} не хватает {needs}")
        continue
    else:
        expenses += (expenses / 100) * 3
        needs += expenses - educational_grant
        print(f"{i}. месяц траты {expenses} не хватает {needs}")