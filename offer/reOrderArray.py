#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


思路一： 空间换时间 建两个数组对号入座
思路二： 冒泡排序思想，设立Flag判断什么时候交换
@author: xiaozuo
"""
# class Solution:
#     def reOrderArray(self, array):
#         # write code here
#         n = len(array)
#         res = []
#         tmp = []
#         for i in array[:]:
#             if i % 2 == 0:
#                 res.append(i)
#             else:
#                 tmp.append(i)
#         return tmp+res


class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)):
            flag = False
            for j in range(len(array) - 1, i, -1):

                if array[j] % 2 == 1 and array[j - 1] % 2 == 0:
                    array[j], array[j-1] = array[j-1], array[j]
                    flag = True
            if flag == False:
                break
        return array

if __name__ == '__main__':
    sol = Solution()
    array = [1,2,3,4,5,6]
    print(sol.reOrderArray(array=array))