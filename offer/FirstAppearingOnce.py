#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
@author: xiaozuo
"""
class Solution:
    # 返回对应char
    def __init__(self):
        self.res = []
    def FirstAppearingOnce(self):
        """字符串中第一个不重复的字符"""
        # write code here
        for key in self.res:
            if self.res.count(key) == 1:
                return key
        return '#'
    def Insert(self, char):
        # write code here
        self.res.append(char)