#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


思路：递归
与运算与短路求值 限制递归条件
@author: xiaozuo
"""
class Solution:
    def Sum_Solution(self, n):
        """1+2+3+4+..n"""
        # write code here
        res = n
        # n > 0 短路运算 and(&&) 与运算
        tmp = n > 0 and self.Sum_Solution(n-1)
        res += tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 100
    print(sol.Sum_Solution(n=n))