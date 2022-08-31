n = int(input("enter the range: "))
list1 = []
for i in range(n):
    if (i>1):
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            list1.append(i)

print(list1)

if (n>1):
    for i in range(2,n):
        if(n%i==0):
            print(i,"is not prime")
            break
    else:
        print(n,"is prime")
else:
    print(n,"is not prime")
