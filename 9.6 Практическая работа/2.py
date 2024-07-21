text = "Пр*ивет к*ак дела"

for i in range(len(text)):
    if text[i] == "*":
        print(f"It's on the {i} position")