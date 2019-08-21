#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

思路：把对字符串中的每个元素都当做起始位置，把其他元素当做以后的位置，然后再同样的进行操作。这样就会得到全排列。


@author: xiaozuo
"""

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss or len(ss) > 9: return []
        res = []
        self.help(ss, res, "")
        return sorted(list(set(res)))

    def help(self, ss, res, tmp):
        if not ss:
            res.append(tmp)
        else:
            for i in range(len(ss)):
                self.help(ss[:i] + ss[i + 1:], res, tmp + ss[i])

if __name__ == '__main__':
    sol = Solution()
    ss = 'abc'
    print(sol.Permutation(ss=ss))

# return sorted(list(set(map(''.join, itertools.permutations(ss)))))  迭代器实现