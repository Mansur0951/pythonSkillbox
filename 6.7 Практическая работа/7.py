num = 3
attempt = int(input("how much attempts you want? "))
tr = 1

while attempt > 0:
    guess_number = int(input("Введите число: "))
    if guess_number < num:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif guess_number > num:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print(f'Congrats man, Число попыток: {tr}')
        break
    attempt -= 1
    tr += 1