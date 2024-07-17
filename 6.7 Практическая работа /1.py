balance = int(input("How much you received? "))

while balance > 5000:
    prod_cost = int(input("Put price: "))
    if (balance < prod_cost) > 0:
        continue
    balance -= prod_cost

print("You dont have money (")