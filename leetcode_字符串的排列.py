# -*- coding: utf-8 -*-
"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").



示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False

思路：滑动窗口 hash 双指针
@author: xiaozuo
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        n1 = len(s1)
        s1 = Counter(s1)
        #print(s1)
        n2 = len(s2)
        if n1>n2:
            return False
        lookup = Counter(s2[:n1])
        #print(lookup)
        l = 0
        for r in range(n1, n2):
            if all(map(lambda x:s1[x]==lookup[x], s1.keys())):
                return True
            lookup[s2[l]] -= 1
            lookup[s2[r]] += 1
            l += 1
        return True if all(map(lambda x:s1[x]==lookup[x], s1.keys())) else False

if __name__ == '__main__':
    sol = Solution()
    s1 = 'ab'
    s2 = 'dfghjba'
    print(sol.checkInclusion(s1=s1, s2=s2))