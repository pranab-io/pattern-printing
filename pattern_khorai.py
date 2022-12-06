
# n is the max number in the pattern
n = int(input("Enter the number of row of below triangle : "))
n2 = n
m = 2
original = n  # to retain the value of n
# outer loop
for i in range(1, 2*n):

    print("\n")
    print(" "*10, end="")  # for pretty printing

    # driver code if row is less than n+1
    if i < original+1:
        # space logic
        for j in range(i):
            print(" ", end=" ")
        # number logic up to 1
        for k in range(n, 0, -1):
            print(k, end=" ")
        n -= 1
        if (n == 0):  # when n==0 or in the 5th row
            n = 2
        # number logic after 1
        for l in range(2, n2+1):
            print(l, end=" ")
        n2 -= 1
        if n2 == 0:
            n2 = 2

    else:
        # space logic
        for j in range(i-m):
            print(" ", end=" ")
        m += 2
        # number logic up to 1
        for k in range(n, 0, -1):
            print(k, end=" ")
        n += 1
        # number logic after 1
        for l in range(2, n2+1):
            print(l, end=" ")
        n2 += 1
print()
