#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

2019.8.20
bilbili笔试考试
@author: xiaozuo
"""
# 第一题 反转单词
s = input()
res = " ".join(s.split(' ')[::-1])
print(res)


# 第二题 最小整数 冒泡算法
n = input()
nums = n.split(',')
s = ''
for j in range(len(nums)-1, 0, -1):
    for i in range(j):
        if int(nums[i] + nums[i+1]) > int(nums[i+1] + nums[i]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
for x in nums:
    s += str(x)
print(s)

# 背包问题
"""
解决思路：动态规划，对每一件物品遍历背包容量，当背包可容纳值大于等于当前物品，与之前已放进去的物品所得价值进行对比，考虑是否需要置换。
            {0                               i = 0 or w = 0           
m[i, w] =   {m[i-1, w]                       wi > w
            {max(vi+ m[i-1, w-wi], m[i-1, w] i > o and w >= wi
"""
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())  # 物品的数量 n = 6
    m = int(sys.stdin.readline().strip())  # 书包能承受的重量 m = 5
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    w = list(map(int, line1.split()))   # 每个物品的重量 [2, 2, 3, 1, 5, 2]
    v = list(map(int, line2.split()))   # 每个物品的价值 [2, 3, 1, 5, 4, 3]

    # 置0 初始化
    value = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            value[i][j] = value[i-1][j]  # 递归的定义
            # 当背包的总容量够放当前物品， 考虑前一状态是否需要置换
            if j >= w[i-1] and value[i][j] < value[i-1][j-w[i-1]] + v[i-1]:
                value[i][j] = value[i-1][j-w[i-1]] + v[i-1]
    print(value[n][m])