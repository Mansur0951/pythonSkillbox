work_hours = int(input("Введите отработанные часы: "))
credit_left = int(input("Введите остаток по кредиту: "))
meal_expenses = int(input("Введите траты на еду: "))

your_expenses = credit_left + meal_expenses

salary = ((200 * work_hours) / (2 ** 3)) + work_hours

if salary >= your_expenses:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")