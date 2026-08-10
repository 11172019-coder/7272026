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



def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum #  返回sum函数
f = lazy_sum(1,3,5,7)
print (f) 
print (f()) 



def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i 
        fs.append(f) #  储存结果含有变量i，直接调用结果会发生变化。
    return fs
f1,f2,f3= count()
print(f1())



def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():    
                return j*j
            return g
        fs.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
    return fs
fs = count()
print (fs[1]())



def createCounter():
    x=0
    def counter():
        nonlocal x
        x = x+1
        return x
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print(L)

L = list(filter(lambda n: n%2==1, range(1, 20)))

print(L)

'''
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def hel():
    print("hello")

f = hel
f()
print(f.__name__)



import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wer(*arg,**kw):       
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*arg,**kw)
    return wer

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
