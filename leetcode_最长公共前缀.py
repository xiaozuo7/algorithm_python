# -*- coding: utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

方法一：借助python的特性  方法二：os自带了 os.path.commonprefix()
@author: xiaozuo
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        for tmp in zip(*strs):
            # print tmp
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

if __name__ == '__main__':
    sol = Solution()
    strs = ['abcd', 'abce','abcg']
    print(sol.longestCommonPrefix(strs))