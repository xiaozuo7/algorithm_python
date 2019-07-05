# -*- coding: utf-8 -*-
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
@author: xiaozuo
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :return: int
        """
        # 设置一个flag 考虑绝对值
        flag = 1 if x >=0 else -1
        abs_x = abs(x)
        # 转换成字符串
        str_x = str(abs_x)
        reverse_str_x = str_x[::-1]
        # 再转换成整形即可
        int_x = int(reverse_str_x)*flag
        if -2**31 <= int_x <= 2**31-1:
            return int_x
        else:
            return 0

if __name__ == '__main__':
    sol = Solution()
    a = 123
    b = -321
    c = 120
    print(sol.reverse(a))
    print(sol.reverse(b))
    print(sol.reverse(c))