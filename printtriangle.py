n = int(input("enter the number : "))

for row in range(1, n+1):
    for col in range(1,n*2):
        if row==n or row+col==n+1 or col-row==n-1:
            print("*",end="")
        else:
            print(end=" ")
    print()