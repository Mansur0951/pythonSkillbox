numSeq = 6
count = 0
flag = True

for i in range(numSeq):
    entNum = int(input("Введите число: "))
    if entNum % 2 != 0:
        count += 1


print(count)
