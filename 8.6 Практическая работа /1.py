soldiers = int(input("How many soldiers we have: "))
totalRules = 4
all_pushups = 0

for i in range(soldiers, 0, -4):
    soldiersAnswer = int(input(f"Soldier {i} tell me the number of rules:n "))
    if soldiersAnswer != totalRules:
        print(f"You have to do some {i * 10} push-ups")
        all_pushups += 10 * i

print(f"All push-ups {all_pushups}")