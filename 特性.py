def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] ==' ':
        s = s[:-1]
    return s
print(trim(' hfehfe   '))



def findminandmax(L):
    Max = L[0]
    Min = L[0]
    for i in L:
        if i >Max:
             Max = i 
        if i < Min:
                Min = i 
    return(Max,Min)
print (findminandmax([1,3,90,5,777,8,]))


l1 =['Hello','World',18,'Apple']
L2 =[s.lower() for s in l1 if isinstance(s,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')



