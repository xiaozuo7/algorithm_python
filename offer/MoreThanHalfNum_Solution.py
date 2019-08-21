#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


思路：hash表解决， 注意：超过一半肯定是中位数
@author: xiaozuo
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        import collections
        d = collections.Counter(numbers)
        n = len(numbers)//2
        for k, v in d.items():
            if v > n:
                return k
        return 0