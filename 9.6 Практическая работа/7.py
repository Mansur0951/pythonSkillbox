shWord = 'sandwich'
# 0 1 2 3 4 5 6 7
new = ''

print(f'Введите зашифрованное сообщение: {shWord}')
# print(len(shWord)) 8

for i in range(len(shWord)):
    if i % 2 == 0 or i == 0:
        new += shWord[i]
    elif i % 2 != 0:
        new += shWord[len(new) - i]

print(new)