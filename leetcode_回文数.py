# -*- coding: utf-8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true

示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

解题思路：转字符串判断
@author: xiaozuo
"""

class Solution:
    def isPalindrome(self, x:int) -> bool:
        return str(x)==str(x)[::-1]


if __name__ == '__main__':
    sol = Solution()
    a = 121
    b = 123
    print(sol.isPalindrome(a))
    print(sol.isPalindrome(b))