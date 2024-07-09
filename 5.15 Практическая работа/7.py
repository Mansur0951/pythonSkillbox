pack_hour = int(input("Введите время от 0 до 23:00: "))
open_hour = 8
close_hour = 22

if (pack_hour >= open_hour and pack_hour < close_hour) and pack_hour not in (14, 15, 10, 11,12, 18,19):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")
