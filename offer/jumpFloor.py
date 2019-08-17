#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

@author: xiaozuo
"""
class Solution:
    def jumpFloor(self, number):
        if number == 0:
            return 0
        elif 0 < number <= 2:
            return number
        else:
            a ,b = 1, 2
            for i in range(2, number):
                a, b = b, a+b
            return b

if __name__ == '__main__':
    sol = Solution()
    number = 4
    print(sol.jumpFloor(number=number))