town = input()
sales = float(input())

result = 0

if town == "Sofia":
    if sales >= 0 and sales <= 500:
        result = sales * 0.05
    elif 500 < sales <= 1000:
        result = sales * 0.07
    elif 1000 < sales <= 10000:
        result = sales * 0.08
    elif sales > 1000:
        result = sales * 0.12

elif town == "Varna":
    if sales >= 0 and sales <= 500:
        result = sales * 0.045
    elif 500 < sales <= 1000:
        result = sales * 0.075
    elif 1000 < sales <= 10000:
        result = sales * 0.10
    elif sales > 1000:
        result = sales * 0.13

elif town == "Plovdiv":
    if  sales >= 0 and sales <= 500:
        result = sales * 0.055
    elif 500 < sales <= 1000:
        result = sales * 0.08
    elif 1000 < sales <= 10000:
        result = sales * 0.12
    elif sales > 1000:
        result = sales * 0.145

else:
    result = "error"

if type(result) == str or sales < 0:
    print("error")
else:
    print("%.2f" % result)
