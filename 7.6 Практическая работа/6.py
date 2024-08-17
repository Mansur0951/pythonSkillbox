enter_numbers = input("Enter numbers: ").split()
temp = 0

for i in enter_numbers:
    if (int(i[0]) * int(i[1])) * 3 == int(i):
        print("good")