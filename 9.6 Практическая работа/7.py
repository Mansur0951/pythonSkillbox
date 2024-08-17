shWord = 'mans'
# 0 1 2 3 4 5 6 7
new = ''

print(f'Введите зашифрованное сообщение: {shWord}')
# print(len(shWord)) 8

for i in range(len(shWord)):
    if i % 2 == 0:
        new += (shWord[0])
        shWord = shWord[1::]
    else:
        new += (shWord[-1])
        shWord = shWord[0:-1]

print(new)
# shacnidw