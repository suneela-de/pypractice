import collections
def missingnumber(nums):
    c = collections.Counter(nums)
    n = len(nums)
    for i in range(n+1):
        if i not in c:
            return i

list1= [3,0,1]
print(missingnumber(list1))