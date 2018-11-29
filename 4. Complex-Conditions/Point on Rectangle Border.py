x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

leftSide = x == x1 and y >= y1 and y <= y2

topSide = y == y1 and x >= x1 and x <= x2

rightside = x == x2 and y >= y1 and y <= y2

bottomSide = y == y2 and x >= x1 and x <= x2

if leftSide or topSide or rightside or bottomSide:
    print("Border")
else:
    print("Inside / Outside")