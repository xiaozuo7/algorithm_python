#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

思路：空树算平衡二叉树 左右子树高度差不能超过2
@author: xiaozuo
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        """判断平衡二叉树"""
        # write code here
        if not pRoot: return True  # 空树也算平衡二叉树
        left = self.depth(pRoot.left)
        right = self.depth(pRoot.right)
        if abs(left - right) > 1:  # 如果左右子树高度相差1以上 则不是
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def depth(self, pRoot):
        """计算树深度的辅助函数"""
        if not pRoot: return 0
        left = self.depth(pRoot.left)
        right = self.depth(pRoot.right)
        return max(left, right) + 1