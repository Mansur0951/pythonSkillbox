reverse_timer = int(input("На сколько секунд поставим таймер? "))

for i in range(reverse_timer, -1, -1):
    ans = int(input("Хотите забрать еду и остановить разогрев или нет. "))
    if ans == 1:
        print("Ваша еда готова, можете забрать")
        print(f"Process was terminated on {i} second")
        break
    elif ans == 0:
        continue

