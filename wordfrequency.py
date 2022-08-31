def frequency(str):
    lst = str.split()
    dictstr = {}

    for i in lst:
        if i not in dictstr.keys():
            dictstr[i]=0
        dictstr[i]+=1
    print(dictstr)

str = "is apple good for health , yes apple is good , goog dot"
frequency(str)