n = int(input("enter the number of rows of the pattern : "))

# outer loop
for i in range(1, n+1):
    print("\n")
    for j in range(0, n-i):
        print(" ", end="")

    # loop for printing number
    for k in range(i, 0, -1):
        print(k, end="")
    for l in range(i-1):
        print(l+2, end="")
print()
