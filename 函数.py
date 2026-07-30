n1 =225
n2 = 1000
print(hex(n1))
print(hex(n2))



def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x < 0:
        return -x
    else:
        return x

print(my_abs(6))



import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    if b*b - 4*a*c<0:
        return '无解'
    if a==0:
        return -c/b
    else:
        return (-b + math.sqrt(b*b - 4*a*c))/(2*a),(-b - math.sqrt(b*b - 4*a*c)) /(2*a)

print(quadratic(0,2,1))
print(quadratic(1,-5,6))



def power(x,n=2):
    g = 1
    while n > 0:
        n = n-1
        g = g*x
    return g

print(power(2,3))



def g (*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum

print(g(1,2,3))



def mul(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum
print(mul(1,2,3,4))



def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
print(fact(68))



