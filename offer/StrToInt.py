#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

输入描述:
输入一个字符串,包括数字字母符号,可以为空


输出描述:
如果是合法的数值表达则返回该数字，否则返回0

示例1
输入
+2147483647
    1a33
输出
2147483647
    0

思路：模拟 ASCII码  ord()返回ASCII码
@author: xiaozuo
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:return 0
        flag = 1 # 标明正负的符号
        add = 0  # 是否进位
        res = 0  # 结果
        if len(s) > 1:
            if s[0] == '+':
                s = s[1:]
            if s[0] == '-':
                flag = -1  # 如果是-，就将flag变成-1
                s = s[1:]   # 将第一个符号，去除
        for i in range(len(s)-1,-1,-1):   # 从后往前遍历字符串
            if s[i] not in "0123456789":    # 先检查是否合法
                return 0
            else:
            # 字符“0”对应的ASCII码为48。对获得的字符串中的每个字符，
            # 求其ASCII码，减去48即为对应位上的数值。
                res += (ord(s[i]) - 48) * (10 ** add)
                add += 1   # 位数每遍历一个字符，就要进一位
        return res * flag

if __name__ == '__main__':
    sol = Solution()
    s = '+123456'
    print(sol.StrToInt(s=s))