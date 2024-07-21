n = 4
ans = 0

for i in range(n):
    ans += (-1) ** i * (1 / 2) ** i
    print(f"n = {i}")

print(ans)