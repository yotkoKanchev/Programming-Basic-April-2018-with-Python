year = input()
holidays = float(input())
weekends_at_home = float(input())
import math
result = 0;
if year == "leap":
    result = 1.15 * (((48 - weekends_at_home) * 3 / 4) + weekends_at_home + (holidays * 2 / 3))
elif year == "normal":
    result = ((48 - weekends_at_home) * 3 / 4) + weekends_at_home + (holidays * 2 / 3)
print(math.floor(result))