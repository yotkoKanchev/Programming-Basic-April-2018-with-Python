h = float(input())
x = float(input())
y = float(input())
result = ""

if x > 0 and x < 3*h and y > 0 and y < h:
    result = "inside"
elif x > h and x < 2*h and y > h and y < 4*h:
    result = "inside"
elif x > h and x < 2 * h and y == h:
    result = "inside"
elif y == 0 and x >= 0 and x <=3 * h:
    result = "border"
elif y == h and x >=0 and x <=h:
    result = "border"
elif y == h and x >= 2*h and x <= 3*h:
    result = "border"
elif y == 4 * h and x >= h and x <= 2*h:
    result = "border"
elif x == 0 and y >= 0 and y <= h:
    result = "border"
elif x == 3 *h and y >= 0 and y <= h:
    result = "border"
elif x == h and y >= h and y <= 4*h:
    result = "border"
elif x == 2*h and y >= h and y <= 4*h:
    result = "border"
else:
    result = "outside"

print(result)