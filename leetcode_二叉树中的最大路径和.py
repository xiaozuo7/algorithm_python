#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

思路：
@author: xiaozuo
"""


def maxPathSum(self, root: TreeNode) -> int:
    self.res = float("-inf")

    def helper(root):
        if not root: return 0
        # 右边最大值
        left = helper(root.left)
        # 左边最大值
        right = helper(root.right)
        # 和全局变量比较
        self.res = max(left + right + root.val, self.res)  # 记录最大值
        # >0 说明都能使路径变大
        return max(0, max(left, right) + root.val)  # 节点与左右子树最大值之和，较差的解直接被舍弃，不会再被用到。

    helper(root)
    return self.res
