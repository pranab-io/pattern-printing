n = int(input("Enter the max number : "))
temp = 1
m = 2
fqn = n  # first quadrant number variable
tqs = 3  # 3rd quadrant space variable
ffqs = 4  # 4th quadrant space var
# this pattern wont work for n<3 or n is even
if (n % 2 == 0) or n < 3:
    print("You entered an odd number or number is less than 3, terminating......")
    exit()

original = n  # to retain the value of n
for i in range(1, 2*original):
    print("\n")
    print("   ",end="")

    # printing first and last line sline
    if i == 1 or i == 2*original-1:
        for v in range(1, 2*original):
            if temp < original+1:
                print(v, end=" ")
                temp += 1
            else:
                print(v-m, end=" ")
                m += 2

    else:
        # The following logic work for i>=2 to i<=8
        if (i < original+1):
            # we will need 4 loops here and 4 loops in else block
            # number , space and max number in top line , space , number

            # for 2nd quadrant number
            for j in range(1, n):
                print(j, end=" ")
            # for 2nd quadrant space
            for k in range(i-1):
                print(" ", end=" ")

            # for first quadrant space
            for l in range(i-2):
                print(" ", end=" ")
            # for first quadrant number
            for m in range(fqn-1, 0, -1):
                print(m, end=" ")

            # updates
            n -= 1
            fqn -= 1

        else:
            # for 3rd quadrant number
            for j in range(1, i-(original-2)):
                print(j, end=" ")
            # for 3rd quadrant space
            for k in range(i-tqs):
                print(" ", end=" ")
            # for 4th quadrant space
            for l in range(i-ffqs):
                print(" ", end=" ")
            # for 4th quadrant number
            for m in range(i-(original-1), 0, -1):
                print(m, end=" ")

            # updates
            ffqs += 2
            tqs += 2

    # setting m=2 and temp=1 again for printing the last line
    m = 2
    temp = 1

print()
print()
