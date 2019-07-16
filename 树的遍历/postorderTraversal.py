# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回它的 后序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]


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
    """后序遍历"""
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        stack = [(root,False)]
        res = []
        while stack:
            cur, vis = stack.pop()
            if vis:
                res.append(cur.val)
            else:
                stack.append((cur, True))     # 后序遍历
                if cur.right:
                    stack.append((cur.right, False))
                if cur.left:
                    stack.append((cur.left, False))
        return res

# 递归写法
#class Solution:
#    def postorderTraversal(self, root: TreeNode) -> List[int]:
#        if not root:return []
#        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []