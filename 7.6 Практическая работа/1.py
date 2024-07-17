enter_numbers = input("Enter numbers: ")
good_num = 0

for i in enter_numbers:
    if int(i) > 0 and int(i) % 2 == 0:
        good_num += 1

print(f"The answer is {good_num}")