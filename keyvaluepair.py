from functools import reduce
def printkeyvalue(dict1):
    list1 = []
    list2 = []
    for key in dict1.keys():
        list1.append(key)
    #list2.append((val for dic in dict1 for val in dic.values()))
    for value in dict1.values():
        if value in list2:
            continue
        else:
          list2.append(value)

    list3=[]
    for num in list2:
        for i in num:
            list3.append(i)

    print(list1)
    print(list2)
    print(list3)

d = {1: [1, 2], 2: 2, 3: [3, 4]}
printkeyvalue(d)
