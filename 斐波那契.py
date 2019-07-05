# -*- coding: utf-8 -*-
"""
斐波那契生成器最简单做法
@author: xiaozuo
"""
def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fib(21):
    print(f'{x}')