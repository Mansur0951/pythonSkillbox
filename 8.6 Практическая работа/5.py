start = -2
stop = 2
step = -1

for i in range(stop, start-1, -1):
    ans = (i ** 3) + 2 * (i ** 2) - (4 * i) + 1
    print(f"В точке {i} функция равна {ans}")
