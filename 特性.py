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



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a =b
        b =a+b
        n = n + 1
    return 'done'
f =fib(9)
print (f)
for i in f:
    print (i)




def tringles(max):
    n=1
    while n <max:
        l1 =list(range(1,n+1))
        l2 =list(range(n-1,0,-1))
        yield (l1+l2)
        n=n+1
    return(None)
g = tringles(9)
for s in g:
    print (s)







