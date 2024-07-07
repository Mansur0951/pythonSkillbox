pass_score = 270

first_exam = int(input("Введите количество баллов по русскому языку: "))
second_exam = int(input("Введите количество баллов по математике: "))
third_exam = int(input("Введите количество баллов по информатике: "))

exam_scores = first_exam + second_exam + third_exam

if exam_scores >= pass_score:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print(f"К сожалению, ты не прошёл на бюджет.\nНе хватило {pass_score - exam_scores} баллов")