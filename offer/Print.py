#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

思路：层序遍历 然后处理以下就可以
@author: xiaozuo
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:return []
        res = []
        queue = [pRoot]
        while queue:
            tmp = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        for i in range(len(res)):
            if i % 2 == 1:  # 奇数反转
                res[i].reverse()
        return res