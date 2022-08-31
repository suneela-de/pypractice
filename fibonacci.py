n = int(input("enter the number: "))
first=0
second=1
list1=[]
for i in range(n):
    list1.append(first)
    #print(first)
    temp = first
    first = second
    second = temp+second
print(list1)
