all_cards = int(input("Введите количество карточек: "))
got = 0
all_list = list(range(1, all_cards+1))

for card in range(1, all_cards):
    found_card = int(input("Введите номер оставшейся карточки: "))
    if found_card in all_list:
        all_list.remove(found_card)

print(f"this is the answer {all_list[0]}")