fruit = input()
day = input()
quantity = float(input())

sum = 0;

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        sum = 2.50 * quantity
        print("%.2f" % sum)
    elif fruit == "apple":
        sum = 1.20 * quantity
        print("%.2f" % sum)
    elif fruit == "orange":
        sum = 0.85 * quantity
        print("%.2f" % sum)
    elif fruit == "grapefruit":
        sum = 1.45 * quantity
        print("%.2f" % sum)
    elif fruit == "kiwi":
        sum = 2.70 * quantity
        print("%.2f" % sum)
    elif fruit == "pineapple":
        sum = 5.50 * quantity
        print("%.2f" % sum)
    elif fruit == "grapes":
        sum = 3.85 * quantity
        print("%.2f" % sum)
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        sum = 2.70 * quantity
        print("%.2f" % sum)
    elif fruit == "apple":
        sum = 1.25 * quantity
        print("%.2f" % sum)
    elif fruit == "orange":
        sum = 0.90 * quantity
        print("%.2f" % sum)
    elif fruit == "grapefruit":
        sum = 1.60 * quantity
        print("%.2f" % sum)
    elif fruit == "kiwi":
        sum = 3.00 * quantity
        print("%.2f" % sum)
    elif fruit == "pineapple":
        sum = 5.60 * quantity
        print("%.2f" % sum)
    elif fruit == "grapes":
        sum = 4.20 * quantity
        print("%.2f" % sum)
    else:
        print(print("error"))

else:
    print("error")