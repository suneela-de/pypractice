n = int(input("enter the number"))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or col==row:
            print("*",end="")
        else:
            print(end=" ")
    print()