n = int(input())

min_number = 1000000000000
for i in range(0, n):

    num = int(input())

    if num <= min_number:
        min_number = num

print(min_number)