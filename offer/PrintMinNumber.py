#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，
打印出这三个数字能排成的最小数字为
321323。
@author: xiaozuo
"""
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        s = ""
        for j in range(len(numbers)-1, 0, -1):
            for i in range(j):
                if int(str(numbers[i]) + str(numbers[i+1])) > int(str(numbers[i+1]) + str(numbers[i])):
                    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        for k in numbers:
            s += str(k)
        return s

if __name__ == '__main__':
    sol = Solution()
    numbers = [3, 32, 321]
    print(sol.PrintMinNumber(numbers=numbers))