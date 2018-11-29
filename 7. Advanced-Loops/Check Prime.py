n = int(input())
is_prime = True
import math
if n < 2:
    print("Not Prime")
else:
    end_in = int(math.sqrt(n))
    for i in range(2, end_in + 1):
        if n/i == n//i:
            is_prime = False
    if is_prime:
        print("Is Prime")
    else:
        print("Not Prime")
