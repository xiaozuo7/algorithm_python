# -*- coding: utf-8 -*-
"""

@author: xiaozuo
"""

def max():
    l = []
    for i in range(3):
        num = input("input a number: ")
        l.append(num)
        l.sort()
    print(l[-1])






if __name__ == '__main__':
    max()