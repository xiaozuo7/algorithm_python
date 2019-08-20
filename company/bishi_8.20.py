#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

2019.8.20
bilbili笔试考试
@author: xiaozuo
"""
# 第一题 反转单词
s = input()
res = " ".join(s.split()[::-1])
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
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    w = list(map(int, line1.split()))
    v = list(map(int, line2.split()))

    value = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            value[i][j] = value[i-1][j]
            if j >= w[i-1] and value[i][j] < value[i-1][j-w[i-1]] + v[i-1]:
                value[i][j] = value[i-1][j-w[i-1]] + v[i-1]
    print(value[n][c])