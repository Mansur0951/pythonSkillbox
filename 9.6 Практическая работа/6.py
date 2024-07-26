all_milk = 0

for i in range(1, 11):
    haveNo = input(f'Put a=свободное стойло, b=занятое: ')
    if haveNo == 'a':
        all_milk += i *2

print(f"During the day we gathered {all_milk} milk")