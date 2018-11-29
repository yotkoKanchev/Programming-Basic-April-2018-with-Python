n = int(input())

max_number = 0

sum = 0
for i in range (0, n):
    num = int(input())
    sum += num
    if num >= max_number:
        max_number = num
if max_number == sum - max_number:
    print("Yes")
    print("Sum = " + str(max_number))
else:
    print("No")
    print("Diff = " + str(abs(max_number - (sum - max_number))))
