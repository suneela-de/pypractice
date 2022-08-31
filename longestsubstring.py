def lengthoflongestsubstring(str):
    cur,sofar,start=0,0,0
    n =len(str)
    i=0
    lookup={}
    while i<n:

        if str[i] not in lookup:
            cur+=1
        else:
            start= max(start,lookup[str[i]])
            cur=i-start

        lookup[str[i]]=i
        sofar = max(sofar,cur)
        i+=1
    return sofar

print(lengthoflongestsubstring('abcabcbb'))