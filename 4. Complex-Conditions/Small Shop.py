product = input()
city = input()
quantity = float(input())

sum = 0

if city == "Sofia":
    if product == "coffee":
        sum = 0.50 * quantity
    elif product == "water":
        sum = 0.80 * quantity
    elif product == "beer":
        sum = 1.20 * quantity
    elif product == "sweets":
        sum = 1.45 * quantity
    elif product == "peanuts":
        sum = 1.60 * quantity

elif city == "Plovdiv":
    if product == "coffee":
        sum = 0.40 * quantity
    elif product == "water":
        sum = 0.70 * quantity
    elif product == "beer":
        sum = 1.15 * quantity
    elif product == "sweets":
        sum = 1.30 * quantity
    elif product == "peanuts":
        sum = 1.50 * quantity

elif city == "Varna":
    if product == "coffee":
        sum = 0.45 * quantity
    elif product == "water":
        sum = 0.70 * quantity
    elif product == "beer":
        sum = 1.10 * quantity
    elif product == "sweets":
        sum = 1.35 * quantity
    elif product == "peanuts":
        sum = 1.55 * quantity

print("%.2f" % sum)
