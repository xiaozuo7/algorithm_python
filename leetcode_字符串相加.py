# -*- coding: utf-8 -*-
"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

    num1 和num2 的长度都小于 5100.
    num1 和num2 都只包含数字 0-9.
    num1 和num2 都不包含任何前导零。
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

思路： 模拟进位
@author: xiaozuo
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if n1==0:return num2
        if n2==0:return num1
        i = n1-1
        j = n2-1
        add = 0
        res = ""
        while i>=0 or j>=0 or add:
            tmp_a = 0
            tmp_b = 0
            if i>=0:
                tmp_a = int(num1[i])
            if j>=0:
                tmp_b = int(num2[j])
            val = tmp_a + tmp_b + add
            res += str(val%10)
            add = val//10
            i -= 1
            j -= 1
        return res[::-1]

if __name__ == '__main__':
    sol = Solution()
    num1 = '123'
    num2 = '458'
    print(sol.addStrings(num1, num2))
