import re
String = """ this is an paragraph
            counting example in 
                python langauage"""

res = len(re.findall(r'\w+', String))
print (str(res))

