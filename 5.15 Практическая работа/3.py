place_in = int(input("Введите место в списке поступающих: "))
if place_in > 10:
    print("К сожалению, вы не поступили.")
else:
    exam_scores = int(input("Введите количество баллов за экзамены: "))
    if place_in >= 1 and place_in <= 10:
        if exam_scores >= 290:
            print("Поздравляем, вы поступили!")
            print("Бонусом вам будет начисляться стипендия.")
        else:
            print("Поздравляем, вы поступили!")
            print("Но вам не хватило баллов для стипендии.")
