height = 15
width = 20

c_height, c_width = 8, 10

for step in range(50):
    command = input(f"W=север, S=юг, A=запад, D=восток\n[Программа]: Марсоход находится на позиции: {c_height} = {c_width} ")
    if command == "W":
        if c_width not in (1, 20):
            c_width -= 1
        else:
            print(f"Марсоход уперся в стену, не может продолжать идти {c_width}")
            continue
    elif command == "S":
        if c_width not in (1, 20):
            c_width += 1
        else:
            print(f"Марсоход уперся в стену, не может продолжать идти {c_width}")
            continue
    elif command == "A":
        if c_height not in (1, 15):
            c_height -= 1
        else:
            print(f"Марсоход уперся в стену, не может продолжать идти {c_width}")
            continue
    elif command == "D":
        if c_height not in (1, 15):
            c_height += 1
        else:
            print(f"Марсоход уперся в стену, не может продолжать идти {c_width}")
            continue
    else:
        print("Incorrect input")
