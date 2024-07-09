numbers = int(input("Input 3 numbers: "))

first = numbers % 10
second = numbers % 100 // 10
third = numbers // 100

if first == second and first == third:
    print("3")
elif first == second and first != third or second == third:
    print("2")
else:
    print("0")