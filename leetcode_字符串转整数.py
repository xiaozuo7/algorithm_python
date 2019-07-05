# -*- coding: utf-8 -*-
"""

假设我们的环境只能存储 32 位大小的有符号整数，
那么其数值范围为 [−2**31,  2**31 − 1]。
如果数值超过这个范围，qing返回  INT_MAX (2**31 − 1) 或 INT_MIN (−2**31) 。
@author: xiaozuo
"""
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi("   +12"))
    print(sol.myAtoi("   -12"))
    print(sol.myAtoi("-"))
    print(sol.myAtoi("-91283472332"))
    print(sol.myAtoi("3.114"))
    print(sol.myAtoi("+-3"))