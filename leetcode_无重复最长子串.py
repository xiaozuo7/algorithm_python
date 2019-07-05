# -*- coding: utf-8 -*-
"""
借助哈希的思想

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

@author: xiaozuo
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        if s is None or len(s) == 0:
            return max_len
        d = {}
        one_max = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            one_max = i - start +1   # 在此次循环中，最大的不重复子串的长度,+1是因为i是从0开始的
            d[s[i]] = i
            max_len = max(max_len, one_max)
        return max_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbbbbb"))
    print(sol.lengthOfLongestSubstring("pwwekydw"))