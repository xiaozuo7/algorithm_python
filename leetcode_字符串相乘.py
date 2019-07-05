# -*- coding: utf-8 -*-
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

说明：

    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

思路：模拟乘法过程
@author: xiaozuo
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        i = len(num1)-1

        def add_one_str(a, b):
            return str(int(a)*int(b))

        def add_str(a, b):
            i = len(a)-1
            j = len(b)-1
            carry_digit = 0
            tmp_res = ""
            while i>=0 or j>= 0 or carry_digit:
                tmp_a = 0
                tmp_b = 0
                if i>= 0:
                    tmp_a = int(a[i])
                if j>= 0:
                    tmp_b = int(b[j])
                all_val = tmp_a + tmp_b + carry_digit
                tmp_res += str(all_val%10)
                carry_digit = all_val//10
                i -= 1
                j -= 1
            return tmp_res[::-1]

        all_add = []
        num_zeros = 0
        while i>=0:
            tmp = add_one_str(num1[i], num2)
            tmp += "0" * num_zeros
            all_add.append(tmp)
            num_zeros += 1
            i -= 1
        ans = ""
        for t in all_add:
            ans = add_str(ans, t)
        return ans

if __name__ == '__main__':
    sol = Solution()
    num1 = '123'
    num2 = '456'
    print(sol.multiply(num1, num2))
