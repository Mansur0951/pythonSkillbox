guess_number = int(input("Введите число: "))
left_side = 50
right_side = 100
att = 1
metka = 50

while True:
    comp_gues = int(input(f"Твоё число равно, меньше или больше, чем число {metka}? "))
    if comp_gues == 1:
        print("I WON")
        break
    elif comp_gues == 2:
        metka = (metka - 101) // 2
    elif comp_gues == 3:
        metka = (metka + 101) // 2

    att += 1

print("counts of attempts", att)

