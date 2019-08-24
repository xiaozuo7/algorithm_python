#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
@author: xiaozuo
"""
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        """正则表达式匹配"""
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 如果模式第二个字符是*
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 如果第一个字符匹配，两种可能1、模式后移两位；2、字符串移1位
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:
                # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
                return self.match(s, pattern[2:])
        # 如果模式第二个字符不是*
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        else:
            return False
