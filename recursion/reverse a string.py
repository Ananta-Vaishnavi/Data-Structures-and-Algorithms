def reverse(str):
    if len(str)==0:
        return 
    else:
        return str[-1]+str[:-1]
st=input()
print(reverse(st))
    
