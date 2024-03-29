# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]


迭代方法实际上是模拟递归的思路
@author: xiaozuo
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代写法
class Solution:
    """前序遍历"""
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        stack = [(root,False)]
        res = []
        while stack:
            cur, vis = stack.pop()
            if vis:
                res.append(cur.val)
            else:
                if cur.right:
                    stack.append((cur.right, False))
                if cur.left:
                    stack.append((cur.left, False))
                stack.append((cur, True))               # 前序遍历
        return res

# 递归写法
#class Solution:
#    def preorderTraversal(self, root: TreeNode) -> List[int]:
#       if not root:return []
#       return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []