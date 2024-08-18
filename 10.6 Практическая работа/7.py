he = 4

for i in range(1, he+1):
    for j in range(i):
        print(' ' * (he - j), end='')
        print('#',end='')
    print()