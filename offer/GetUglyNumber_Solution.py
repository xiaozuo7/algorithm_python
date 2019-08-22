#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
丑数

把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


@author: xiaozuo
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        if index == 1:
            return 1
        res = [1]     # 用于保存排好序的丑数 都是由2，3，5乘得到的
        tmp_2, tmp_3, tmp_5 = 0, 0, 0  # 2，3，5的位置
        for i in range(1, index):
            if res[tmp_2] * 2 <= res[i-1]:
                tmp_2 += 1
            if res[tmp_3] * 3 <= res[i-1]:
                tmp_3 += 1
            if res[tmp_5] * 5 <= res[i-1]:
                tmp_5 += 1
            cur = min(res[tmp_2] * 2, res[tmp_3] * 3, res[tmp_5] * 5)
            res.append(cur)
            # print(res)
        return res[index-1]

if __name__ == '__main__':
    sol = Solution()
    index = 7
    print(sol.GetUglyNumber_Solution(index=index))