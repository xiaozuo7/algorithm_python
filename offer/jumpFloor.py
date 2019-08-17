#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

思路：递归 参考fibnacci数列
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