n = int(input())

max_number = - 1000000000000
for i in range(0, n):

    num = int(input())

    if num >= max_number:
        max_number = num

print(max_number)