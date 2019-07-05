# -*- coding: utf-8 -*-
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

思路：回溯递归
@author: xiaozuo
"""

class Solution:
    def partition(self, s: str):
        if not s:return [[]]
        n = len(s)
        res = []
        for i in range(n):
            tmp = s[:i+1]
            if tmp == tmp[::-1]:
                for j in self.partition(s[i+1:]):
                    res.append([tmp]+j)
        return res

if __name__ == '__main__':
    sol=Solution()
    s = 'abc'
    print(sol.partition(s))