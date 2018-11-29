num = int(input())

if num == 100:
    print("one hundred")
elif num == 0:
    print("zero")
elif num == 10:
    print("ten")
elif num == 11:
    print("eleven")
elif num == 12:
    print("twelve")
elif num == 13:
    print("thirteen")
elif num == 14:
    print("fourteen")
elif num == 15:
    print("fifteen")
elif num == 16:
    print("sixtheen")
elif num == 17:
    print("seventeen")
elif num == 18:
    print("eighteen")
elif num == 19:
    print("nineteen")

else:
    zero = "zero"
    one = "one"
    two = "two"
    three = "three"
    four = "four"
    five = "five"
    six = "six"
    seven = "seven"
    eight = "eight"
    nine = "nine"
    twenty = "twenty"
    thirty = "thirty"
    forty = "forty"
    fifty = "fifty"
    sixty = "sixty"
    seventy = "seventy"
    eighty = "eighty"
    ninety = "ninety"

    oldThens = num // 10
    oldOnes = num % 10

    thens = oldThens
    ones = oldOnes

    if thens == 2:
        thens = twenty
    elif thens == 3:
        thens = thirty
    elif thens == 4:
        thens = forty
    elif thens == 5:
        thens = fifty
    elif thens == 6:
        thens = sixty
    elif thens == 7:
        thens = seventy
    elif thens == 8:
        thens = eighty
    elif thens == 9:
        thens = ninety

    if ones == 1:
        ones = one
    elif ones == 2:
        ones = two
    elif ones == 3:
        ones = three
    elif ones == 4:
        ones = four
    elif ones == 5:
        ones = five
    elif ones == 6:
        ones = six
    elif ones == 7:
        ones = seven
    elif ones == 8:
        ones = eight
    elif ones == 9:
        ones = nine


    if num >= 0 and num <= 100:
        if oldOnes == 0:
            print(thens)

        if num < 10:
            print(ones)

        if oldOnes != 0 and oldThens != 0:
            print(thens + " " + ones)
    else:
        print("invalid number")