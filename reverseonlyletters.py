def reverseonlyletters(str):
    left,right=0,len(str)-1
    s = list(str)

    while left<right:
        while not s[left].isalpha() and left<right:
            left+=1
        while not s[right].isalpha() and left<right:
            right-=1

        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1

    return "".join(s)

def reverseonlywords(str):
    lst = str.split()
    lstreverse=[]

    for i in lst:
        lstreverse.append(reverseonlyletters(i))

    return " ".join(lstreverse)

print(reverseonlywords('abc defg'))

