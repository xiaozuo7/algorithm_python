# -*- coding: utf-8 -*-
"""
斐波那契生成器最简单做法
@author: xiaozuo
"""
def fib(n):
    a,b = 1,1
    for i in range(n):
        a,b = b, a+b
    return a

if __name__ == '__main__':
    print(fib(2))