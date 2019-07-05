# -*- coding: utf-8 -*-
"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

来源：力扣（LeetCode）

@author: xiaozuo
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        self.orderTraversal(root, res)
        return res[k - 1]

    def orderTraversal(self, root, res):
        if not root: return []
        self.orderTraversal(root.left, res)
        res.append(root.val)  # 若返回节点， 不返回值则 只需要root
        self.orderTraversal(root.right, res)

class Solution1:
    def kthSmallest(self, root, k):
        if not root:return None
        res = []
        stack = [(root, False)]
        while stack:
            cur, vis = stack.pop()
            if vis:
                res.append(cur) # 如果是返回值则是 cur.val
            else:
                if cur.right:
                    stack.append((cur.right, False))
                stack.append((cur, False))
                if cur.left:
                    stack.append((cur.left, False))
        return res[k-1]