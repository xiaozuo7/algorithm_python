# -*- coding: utf-8 -*-
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

使用动态规划,用空间换时间,把问题拆分
这道题, 如何划分小问题, 我们可以先把所有长度最短为1的子字符串计算出来，
根据起始位置从左向右, 这些必定是回文. 然后计算所有长度为2的子字符串,
再根据起始位置从左向右. 到长度为3的时候, 我们就可以利用上次的计算结果：
如果中心对称的短字符串不是回文, 那长字符串也不是, 如果短字符串是回文,
那就要看长字符串两头是否一样. 这样, 一直到长度最大的子字符串, 我们就把整个字符串集穷举完了.

@author: xiaozuo
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


        max_length = 0
        start = 0
        for i in range(len(s)):
            if i - max_length >= 1 and s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1]:
                # 记录当前开始位置
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i-max_length: i+1] == s[i-max_length: i+1][::-1]:
                start = i - max_length
                # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
                max_length += 1
        # 返回最长回文子串
        return s[start: start + max_length]


if __name__ == '__main__':
    s = "abcba"
    # s = "cbbd"
    sl = Solution()
    print(sl.longestPalindrome(s))