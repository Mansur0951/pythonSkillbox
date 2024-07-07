num = int(input("Enter a number: "))

if num < 0:
    print(f"Вы ввели {num}, answer is {abs(num)}")
else:
    print(f"Вы ввели {num}, answer is {num}")