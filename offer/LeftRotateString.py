#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，
请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。

思路：
先旋转 0-n
再旋转 n-len(s)
再旋转 0-len(s)
@author: xiaozuo
"""
class Solution:
    def LeftRotateString(self, s, n):
        """左旋转字符串"""
        # write code here
        if not s or n < 0:return s
        s = list(s)
        self.swap(s, 0, n-1)      # 0 - n
        self.swap(s, n, len(s)-1) # n - len(s)
        self.swap(s, 0, len(s)-1) # 0 - len(s)
        return ''.join(s)

    def swap(self, s, l, r):
        """旋转函数"""
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    sol = Solution()
    s = 'abcXYZdef'
    print(sol.LeftRotateString(s=s, n=3))