x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

import math

area = abs(x1 - x2) * abs(y1 - y2)
perimeter = abs(x1 - x2) * 2 + abs(y1 - y2) * 2
print(area)
print(perimeter)
