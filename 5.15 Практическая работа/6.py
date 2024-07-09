flats_price = int(input("Put flat's price: "))
size_flat = int(input("Put flat's size: "))

if flats_price <= 10000000 and size_flat >= 100:
    print("Fits us")
elif flats_price <= 7000000 and size_flat <= 80:
    print("Fits us")
else:
    print("dont fit us anymore")