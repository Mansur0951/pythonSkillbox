width = 20
height = 10

for i in range(height):
    for j in range(width):
        if j == 0:
            print('|', end='')
        elif j == 19:
            print('|', end='')
        elif i == 0:
            print('-', end='')
        elif i == 9:
            print('-', end='')
        else:
            print(' ', end='')
    print()