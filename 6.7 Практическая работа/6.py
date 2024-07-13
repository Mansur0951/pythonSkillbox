invest = 1400 # x
proc_rise = 10 # p
expect_money = 10000 # y
year = 1

while invest < expect_money:
    invest += (invest // 100) * 10
    year += 1

print(year)
print(invest)