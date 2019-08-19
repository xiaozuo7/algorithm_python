#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(
注意: 在返回值的list中，数组长度大的数组靠前)

题目的意思是: 给一个数  从根结点往下搜索 一条路经上的和等于这个数就返回这个路径列表
思路:递归 如果只有根结点且等于这个数 就返回根结点 否则返回空列表
然后 递归左子树和右子树搜索
@author: xiaozuo
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        if not root.left and not root.right and root.val == expectNumber: # 只有根结点且等于target
            return [[root.val]]
        else:
            left = self.FindPath(root.left, expectNumber - root.val) # 递归左子树 target - root.val
            right = self.FindPath(root.right, expectNumber - root.val) # 递归右子树 target - root.val
            for i in left + right:
                res.append([root.val] + i)
            return res
        