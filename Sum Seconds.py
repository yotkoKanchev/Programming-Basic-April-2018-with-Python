firstScore = int(input())
secondScore = int(input())
thirdScore = int(input())

minutes = 0
seconds = 0

totalSeconds = firstScore + secondScore + thirdScore

minutes = totalSeconds // 60
seconds = totalSeconds % 60

if seconds < 10:
    print(str(minutes) +":0" + str(seconds))

else:
    print(str(minutes) + ":" + str(seconds))