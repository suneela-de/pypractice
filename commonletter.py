def commonletters(First,Second):
    SetFirst = set(First)
    SetSecond = set(Second)
    lst = SetFirst & SetSecond
    print(lst)

commonletters('SUNIL','LEELA')