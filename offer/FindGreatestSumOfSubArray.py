#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
连续子数组最大和

例如:{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8
(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和(子向量的长度至少是1)

思路：tmp比较加入新的数后的情况变化 res保存最大结果
@author: xiaozuo
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) < 2:
            return array
        else:
            res = tmp = array[0]
            for i in range(1, len(array)):
                tmp = max(array[i], array[i] + tmp)
                # print("tmp:{}".format(tmp))
                res = max(tmp, res)
                # print("res:{}".format(res))
            return res
if __name__ == '__main__':
    sol = Solution()
    arr = [6,-3,-2,7,-15,1,2,2]
    print(sol.FindGreatestSumOfSubArray(array=arr))