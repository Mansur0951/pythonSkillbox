boysCount = 5
girlsCount = 5
answer = ''

if (boysCount > 2 * girlsCount) or (girlsCount > 2 * boysCount):
    print("Dont have solution")
elif boysCount >= girlsCount:
    k = boysCount + girlsCount
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girlsCount - k):
        answer += 'BG'
else:
    k = girlsCount - boysCount
    for gbg in range(k):
        answer += "GBG"
    for gb in range(boysCount - k):
        answer += 'GB'