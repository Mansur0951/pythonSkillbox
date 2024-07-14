guess_number = int(input("Введите число: "))
left_side = 1
right_side = 100
att = 1
metka = 50

while True:
    print(f"Твоё число равно, меньше или больше, чем число {metka}?")
    comp_gues = int(input(f"1 — равно, 2 — больше, 3 — меньше "))
    if comp_gues == 1:
        print("I WON")
        break
    elif comp_gues == 2: #more
        left_side = metka
        metka = (metka + right_side) // 2
    elif comp_gues == 3: #less
        right_side = metka
        metka = (left_side + right_side) // 2

    att += 1

print("counts of attempts", att)

