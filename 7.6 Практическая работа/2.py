all_salary = 0

for i in range(1, 13):
    enter_salary = int(input("Enter your salary: "))
    all_salary += enter_salary

print(f"The avarage salary for year is {all_salary // 12}")