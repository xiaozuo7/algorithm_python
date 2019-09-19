# -*- coding: utf-8 -*-
"""
斐波那契数列几种实现方法
斐波那契:0 1 1 2 3 5 8 13
又称黄金分割数列
fo=0  n=0
f1=1  n=1
fn=f[n-1]+f[n-2] n>=2
"""

#方法一
def fib_1(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib_1(10))  #求第10个斐波那契数列


#递归方法
def fib_2(m):
    if m == 1 or m == 2:
        return 1
    return fib_2(m-1)+fib_2(m-2)
print(fib_2(10))


#输出指定个数的斐波那契数列
def fib_3(p):
    if p == 1:
        return[1]
    fibs=[1,1]
    for i in range(2,p):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(fib_3(10))

#使用循环的方法做 时间用时最短
def fib_4(n):
    if n < 2:
        return n
    else:
        c = 0
        a = 0
        b = 1
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return(c)

print(fib_4(10))

#yield 语法糖做法 最省内存
def fib_5(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fib_5(100):
    print(x)