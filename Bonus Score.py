num = int(input())
bonus = 0
result = 0
if num <= 100:
    bonus = 5
    result = num + bonus

elif num <= 1000:
    bonus = 0.2 * num
    result = num + bonus

elif num > 1000:
    bonus = 0.1 * num
    result = num + bonus

if num % 2 == 0:
    result = result + 1
    bonus+=1

elif num %10 == 5:
    result = result + 2
    bonus+=2

print(bonus)
print(result)
