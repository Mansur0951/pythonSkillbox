saved_greec = 100
expences = 4

month = int(input("Прогноз гречка, введите колл-во месяцев; "))

for i in range(month):
    saved_greec -= expences

print(f"After {month} months i'll have {saved_greec}")