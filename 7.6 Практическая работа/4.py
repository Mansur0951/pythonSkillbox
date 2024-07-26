grades_seq = input("Enter grades: ")
fifth_gr = 0
forth_gr = 0
third_gr = 0

for i in grades_seq:
    if int(i) == 5:
        fifth_gr += 1
    elif int(i) == 4:
        forth_gr += 1
    elif int(i) == 3:
        third_gr += 1

print(f"Больше всего у нас {max(int(fifth_gr), int(forth_gr), int(third_gr))}")
if fifth_gr > forth_gr and fifth_gr > third_gr:
    print(f"Больше всего у нас с оценкой 5 {fifth_gr}")
elif forth_gr > fifth_gr and forth_gr > third_gr:
    