#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
@author: xiaozuo
"""
class Solution:
    def __init__(self):
        self.res = []
    def Insert(self, num):
        # write code here
        self.res.append(num)
        self.res.sort()
    def GetMedian(self, res):
        """数据流中的中位数"""
        # write code here
        n = len(self.res)
        if n % 2 == 1:
            return self.res[n // 2]
        else:
            return (self.res[n // 2] + self.res[n //2 - 1]) / 2.0