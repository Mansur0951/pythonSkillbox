rowCount = int(input("Колл-во рядов; "))
seatsCount = int(input("Колл-во сидений; "))
metrBetween = int(input("Колл-во метров между рядами; "))


for i in range(rowCount):
    print("=" * seatsCount, "*" * metrBetween, "=" * seatsCount)