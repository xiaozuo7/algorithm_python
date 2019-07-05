# -*- coding: utf-8 -*-
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

思路： 递归 DFS遍历
@author: xiaozuo
"""

class Solution:
    def restoreIpAddresses(self, s):
        self.res = []
        tmpList = []
        self.dfs(s, tmpList)
        return self.res

    # dfs遍历，s为待处理字段，tmp存储所有ip小段
    def dfs(self, s, tmpList):
        if len(tmpList)==4: # 递归出口，凑够4段
            if len(s)==0:   # s没有剩余，说明找到一个合法ip，否则返回
                self.res.append('.'.join(tmpList))
            return
        for i in range(1, 4): # 遍历取s的头，长度从1到3
            if i <= len(s):   # 防止越界
                if int(s[:i]) > 255:  # 数字超出范围
                    return
                elif i>1 and s[0]=="0": # 除去0开头，且长度大于1情况
                    return
                self.dfs(s[i:], tmpList + [s[:i]]) # 截断s，并将本次截取内容写入tmp

if __name__=='__main__':
    sol = Solution()
    s = "25525511135"
    print(sol.restoreIpAddresses(s))