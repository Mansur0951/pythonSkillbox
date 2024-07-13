print("Начался восьмичасовой рабочий день.")
sum_tasks = 0
grocery = False

for i in range(1, 3):
    print(f"{i} hour")
    task_num = int(input("Сколько задач решит Максим? "))
    wife_call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if wife_call == 1:
        grocery = True
    sum_tasks += task_num

print(f"Рабочий день закончился. Всего выполнено задач: {sum_tasks}")
if grocery:
    print("Нужно зайти в магазин.")