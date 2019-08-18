#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

思路：判断是否是子结构的时候，如果当前值相等，需要进行左右值是否相等的判断；如果当前值不等，则判断Root1的左右子树是否包含Root2.
@author: xiaozuo
"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        """用来初始化"""
        if pRoot2 == None or pRoot1 == None: return False
        return self.help(pRoot1, pRoot2)

    def help(self, p1, p2):
        """判断是否为子树"""
        if p2 == None: return True
        if p1 == None:
            return p1 == p2
        flag = False
        if p1.val == p2.val:
            flag = self.help(p1.left, p2.left) and self.help(p1.right, p2.right)  # 匹配子树是否相等
        return flag or self.help(p1.left, p2) or self.help(p1.right, p2)  # 判断左右子树是否还包含