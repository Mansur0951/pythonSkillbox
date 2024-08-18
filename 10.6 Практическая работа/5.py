tempSum = 0
maxOne = 0

for i in range(3):
    enterNum = int(input('Enter number: '))
    tempSum = sum([int(i) for i in str(enterNum)])

    if tempSum > maxOne:
        maxOne = tempSum

print(maxOne)