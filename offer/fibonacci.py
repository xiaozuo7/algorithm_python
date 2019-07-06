# -*- coding: utf-8 -*-
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
@author: xiaozuo
"""


class Solution:
    """斐波那契"""
    def Fibonacci(self, n):
        # write code here
        if n == 0:return 0
        a,b = 1,1
        for i in range(1,n):
            a,b = b,a+b
        return a