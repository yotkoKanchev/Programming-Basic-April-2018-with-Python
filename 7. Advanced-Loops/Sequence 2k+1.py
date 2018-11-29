n = int(input())

num1 = 1
for i in range (0, n):
    print(num1)
    num1 = num1 * 2 + 1
    if num1 > n:
        break
