correctAns = 0

for i in range(10):
    ans = input("Put the word")
    if ans == 'Карамба':
        correctAns += 1

print(f"On ship allowed only {correctAns} people")