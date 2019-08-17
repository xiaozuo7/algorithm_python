#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路一：0, 1, 2, 4, 16  2**(number-1)
思路二：快速幂 1 << (number-1)

<< >> 运算符 与2的幂次方有关  exm:  1 << 4 读作 将 1划算成二进制, 将1左移动四位  0001(1) 变成 10000(16)
@author: xiaozuo
"""
class Solution:
    def jumpFloorII_1(self, number):
        # write code here
        return pow(2, number-1)

    def jumpFloorII_2(self, number):
        return 1 << (number-1)

if __name__ == '__main__':
    sol = Solution()
    number = 5
    print(sol.jumpFloorII_1(number=number))
    print(sol.jumpFloorII_2(number=number))