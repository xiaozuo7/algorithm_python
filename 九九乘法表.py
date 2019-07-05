# -*- coding: utf-8 -*-
"""
一行写出9X9乘法表

f-string的高级用法 y:2是为了让输出对齐
@author: xiaozuo
"""



print('\n'.join([' '.join([f'{x}*{y}={x * y:2}' for x in range(1, y+1)]) for y in range(1, 10)]))