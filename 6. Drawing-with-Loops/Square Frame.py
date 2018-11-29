n = int(input())

print("+ ", end="")

for i in range(1,n-1):
    print("- ", end="")

print("+", end="")
print()

for i in range(1, n-1):
    print("| ", end="")

    for j in range(1,n -1):
        print("- ", end="")
    print("|", end="")
    print()

print("+ ", end="")

for i in range(1,n-1):
    print("- ", end="")

print("+", end="")