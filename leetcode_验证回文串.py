# -*- coding: utf-8 -*-
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false

正常思路： 双指针 py人的思路 filter过滤 也可用re
@author: xiaozuo
"""
import  re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''.join(filter(str.isalnum,s)).lower()
        return res == res[::-1]
    def isHuiwen(self, s):
        regex = re.compile('\W+')
        res = regex.sub('', s.lower())
        return res == res[::-1]
if __name__ == '__main__':
    sol=Solution()
    s="A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))
    print(sol.isHuiwen(s))