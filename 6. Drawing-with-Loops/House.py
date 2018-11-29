n = int(input())

if n % 2 == 0:
    stars = 2

    for row in range(1, n//2 + 1):
        dashes = n//2 - row
        print("-"*dashes + "*"*stars + "-"*dashes)
        stars += 2
else:
    stars = 1
    for row in range(1, (n//2 + 2)):
        dashes = (n+1) // 2 - row
        print("-" * dashes + "*"*stars + "-" * dashes)
        stars += 2
for row in range(0, n // 2):
    print("|" + "*"*(n-2) + "|")



