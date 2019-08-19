#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：后续遍历 最后一个数是root  前面可以分为 左子树 (比root小) 和 右子树(比root大) 递归判断即可
@author: xiaozuo
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:return False
        n = len(sequence)
        for i in range(n):
            global index
            index = i
            if sequence[i] > sequence[-1]:
                break
        for j in range(index, n):
            if sequence[j] < sequence[-1]:
                return False
        left = True
        right = True
        if len(sequence[:index]) > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index:-1]) > 0:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right

if __name__ == '__main__':
    sol = Solution()
    test1 = [1, 2, 3, 8, 7, 6, 5]
    test2 = [1, 2, 8, 4, 5, 6, 7]
    print(sol.VerifySquenceOfBST(sequence=test1))
    print(sol.VerifySquenceOfBST(sequence=test2))