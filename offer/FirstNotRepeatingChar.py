#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
第一次只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

思路：hash  lambda count
@author: xiaozuo
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        d = dict()
        n = len(s)
        for i in s:
            d[i] = d.get(i, 0) + 1
            # print(d)
        # 因为字典无序， 所有不能直接遍历字典
        for j in range(n):
            if d.get(s[j]) == 1:
                return j
        return -1

    # return s.index(list(filter(lambda x:s.count(x) == 1, s))[0]) if s else -1

if __name__ == '__main__':
    sol = Solution()
    s = 'google'
    print(sol.FirstNotRepeatingChar(s=s))