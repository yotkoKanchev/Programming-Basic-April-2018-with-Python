n = int(input())
if n == 1:
    print("*")
elif n == 2:
    print("**")
else:
    stars = 0
    dashes = 0
    mid_dashes = 0

    if n % 2 ==0:
        stars = 2
        dashes = n//2 - 1
        mid_dashes = 2
        print("-" * dashes + "*" * stars + "-" * dashes)
        dashes = (n-4)//2
        stars = 1
        for row in range(0, n//2 - 1):
            print("-" * dashes + "*" * stars + "-" * mid_dashes + "*" * stars + "-" * dashes)
            mid_dashes+=2
            dashes-=1

        mid_dashes = n-4
        dashes = 1
        for row in range(0,n//2 - 1):
            print("-" * dashes + "*"*stars + "-"*mid_dashes + "*"* stars + "-"*dashes)
            mid_dashes -= 2
            dashes += 1

    else:
        stars = 1
        dashes = n//2
        mid_dashes = 1
        print("-" * dashes + "*" * stars + "-" * dashes)
        dashes = n//2 - 1
        stars = 1
        for row in range(0, n // 2):
            print("-" * dashes + "*" * stars + "-" * mid_dashes + "*" * stars + "-" * dashes)
            mid_dashes += 2
            dashes-=1

        dashes = 1
        mid_dashes = n-4
        for row in range(1,n//2):
            print("-" * dashes + "*" * stars + "-" * mid_dashes + "*" * stars + "-" * dashes)
            mid_dashes -= 2
            dashes += 1

        stars = 1
        dashes = n // 2
        mid_dashes = 1
        print("-" * dashes + "*" * stars + "-" * dashes)