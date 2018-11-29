n = int(input())

while n < 1 or n > 100:
    print("Invalid number!")
    print("Еnter a number in the range [1...100]: ")
    n = int(input())

print(f"The number is: {n}")