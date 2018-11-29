hours = int(input())
minutes = int(input())

inMinutesFinal = hours * 60 + minutes + 15

newHours = inMinutesFinal // 60
if newHours > 23:
    newHours = newHours - 24

newMinutes = inMinutesFinal % 60

if newMinutes < 10:
    print(str(newHours) + ":0" + str(newMinutes))
else:
    print(str(newHours) + ":" + str(newMinutes))