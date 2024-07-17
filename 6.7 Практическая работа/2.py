name = input("Enter your name: ")
debt = int(input("How much u owe: "))

while debt != 0:
    print(f"{name}, ваша задолженность составляет {debt} рублей.")
    money = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    if money >= debt:
        print("Отлично, Василий! Вы погасили долг. Спасибо!")
        break
    print(f"Маловато, {name}. Давайте ещё раз.")