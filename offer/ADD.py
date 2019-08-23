#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

0xffffffff是多少？

0xffffffff表示的是一个十六进制数

1.将其转换为十进制数
    0xffffffff=16x10^7+16x10^6+...+16x10^0=4294967295

2.将其转换为二进制数
    十六进制转换为二进制就是直接把每位转换成二进制就可以了
    f(15)变成二进制：1111，则
    0xffffffff = 1111 1111 1111 1111 1111 1111 1111 1111 (8个F的二进制形式, 一个F占4个字节 ) 
    即32位数都是1的二进制数

0x代表16进制，后面是数字，十进制是4294967295

@author: xiaozuo
"""
class Solution:
    def Add(self, num1, num2):
        """不用加减乘除做加法"""
        # write code here
        while num2 != 0:
            tmp = num1 ^ num2
            # print("tmp:", tmp)
            num2 = (num1 & num2) << 1
            # print("num2:", num2)
            # print("before:", num1)
            num1 = tmp & 0xFFFFFFFF
            # print("after:", num1)
        return num1 if num1 >> 31 == 0 else num1 - 4294967296

if __name__ == '__main__':
    sol = Solution()
    num1 = 2
    num2 = 3
    print(sol.Add(num1=num1, num2=num2))