type = input()
rows = int(input())
cols = int(input())
result = 0
if type == "Premiere":
    result = rows * cols * 12.00
elif type == "Normal":
    result = rows * cols * 7.50
elif type == "Discount":
    result = rows * cols * 5.00
print("{0:.2f} leva".format(result))