#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


@author: xiaozuo
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.help(pRoot.left, pRoot.right)

    def help(self, left, right):
        if not left and not right:  # 左右节点都没有
            return True
        if not left or not right:  # 有其中一个结点 另一个没有 不对称
            return False
        if left.val == right.val:  # 比较值
            return self.help(left.left, right.right) and self.help(left.right, right.left)  # 递归下一个值
        return False