num = float(input())
enteredValue = input()
expectedVal = input()
inMeters = 0
if enteredValue == "m":
    inMeters = num
elif enteredValue == "mm":
    inMeters = num / 1000
elif enteredValue == "cm":
    inMeters = num / 100
elif enteredValue == "mi":
    inMeters = num / 0.000621371192
elif enteredValue == "in":
    inMeters = num / 39.3700787
elif enteredValue == "km":
    inMeters = num / 0.001
elif enteredValue == "ft":
    inMeters = num / 3.2808399
elif enteredValue == "yd":
    inMeters = num / 1.0936133

result = 0;

if expectedVal == "m":
    result = inMeters
elif expectedVal == "mm":
    result = inMeters * 1000
elif expectedVal == "cm":
    result = inMeters * 100
elif expectedVal == "mi":
    result = inMeters * 0.000621371192
elif expectedVal == "in":
    result = inMeters * 39.3700787
elif expectedVal == "km":
    result = inMeters * 0.001
elif expectedVal == "ft":
    result = inMeters * 3.2808399
elif expectedVal == "yd":
    result = inMeters * 1.0936133

print(str(result) + " " + expectedVal)
