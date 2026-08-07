'''
L = []
def f(x):
    return x*x
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)



def f (x):
    return x*x
r = list(map(f, [1,2,3,4,5,6,7,8,9]))
for i in r:
    print(i)
print(r)        



from functools import reduce 
def mul(x,y):
    return x*y
def prod(L):
    return reduce (mul,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



def normalize(name):
    for i,ch in enumerate(name):
        if i==0 and ord(ch)>=97 and ord(ch)<=122:
            name=chr(ord(ch)-32)+name[1:]
        if i!=0 and ord(ch)>=65 and ord(ch)<=90:
            name=name[:i]+chr(ord(ch)+32)+name[i+1:]
    return name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



from functools import reduce

DIGITS ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    def char_to_num(ch):
        return DIGITS[ch]

    def merge(x, y):
        return x * 10 + y

    if '.' in s:
        left, right = s.split('.')
        left_num = reduce(merge, map(char_to_num, left))
        right_num = reduce(merge, map(char_to_num, right))
        scale = 10 ** len(right)
        return left_num + right_num / scale
    else:
        return reduce(merge, map(char_to_num, s))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



def is_palindrome(n):
    n = str(n)
    return n[:] == n[::-1]


print( list(filter(is_palindrome, range(1, 1000))))

# 测试:
result = list(filter(is_palindrome, range(1, 200)))
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]

if result == expected:
    print('测试成功!')
else:
    print('测试失败!')



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):#  提取姓名
    return t[0]
def by_score(t):#  提取分数
    return t[1]
#  按名字排序
L1 = sorted(L, key=by_name)
print(L1)
#  按分数排序
L2 = sorted(L, key=by_score)
print(L2)


'''
