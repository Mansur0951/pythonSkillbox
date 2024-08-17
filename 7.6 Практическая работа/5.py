first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
circle = 0
all_krat = 0

for i in range(first_num, second_num+1):
    if i % 3 == 0:
        circle += 1
        all_krat += i

print(f"The answer is {all_krat / circle}")