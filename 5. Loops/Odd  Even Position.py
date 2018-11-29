n = int(input())

odd_sum = 0
odd_min = 1000000000000
odd_max = -1000000000000
even_sum = 0
even_min = 10000000000000
even_max = -10000000000000

for i in range(0, n):
    num = float(input())

    if i % 2 == 0:
        odd_sum += num
        if num >= odd_max:
            odd_max = num
        if num <= odd_min:
            odd_min = num

    else:
        even_sum+= num
        if num >= even_max:
            even_max = num
        if num <= even_min:
            even_min = num

if even_min ==10000000000000:
    even_min = "No"
if even_max == -10000000000000:
    even_max = "No"
if odd_min == 1000000000000:
    odd_min = "No"
if odd_max == -1000000000000:
    odd_max = "No"
if odd_sum % 1 != 0 and (n != 0 or n != 1):
    print(f"OddSum={odd_sum},")
else:
    print(f"OddSum={int(odd_sum)},")
if odd_min % 1 != 0 and (n != 0 or n != 1):
    print(f"OddMin={odd_min},")
else:
    print(f"OddMin={int(odd_min)},")
if odd_max % 1 != 0 and (n != 0 or n != 1):
    print(f"OddMax={odd_max},")
else:
    print(f"OddMax={int(odd_max)},")
if even_sum % 1 != 0 and (n != 0 or n != 1):
    print(f"EvenSum={even_sum},")
else:
    print(f"EvenSum={int(even_sum)},")
if even_min % 1 != 0 and (n != 0 or n != 1):
    print(f"EvenMin={even_min},")
else:
    print(f"EvenMin={int(even_min)},")
if even_max % 1 != 0 and (n != 0 or n != 1):
    print(f"EvenMax={even_max},")
else:
    print(f"EvenMax={int(even_max)},")




