# -*- coding: utf-8 -*-
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G


思路：
每一个Z字的首字母差，numRows*2-2 位置 比如第一行 三个数字 1 2n-1 4n-3
除去首尾两行，每个 Z 字有两个字母，索引号关系为，一个为 i，另一个为 numsRows*2-2-i

@author: xiaozuo
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows == 1: return s

        split_s_len = numRows * 2 - 2 # 首尾字母之差
        data = []
        for i in range(0, len(s), split_s_len): # i=0, 4, 8, 12
            data.append(s[i:i + split_s_len]) #0-4 4-8 8-12 12-16
        #print(data)
        res = ""
        for i in range(numRows):
            for tmp in data:
                if i < len(tmp): # len(tmp)=4
                    if i == 0 or i == numRows - 1: # 第一行或者最后一行
                        res += tmp[i]
                    else:
                        res += tmp[i]
                        if split_s_len - i < len(tmp):
                            res += tmp[split_s_len - i]
        return res

if __name__ == '__main__':
    sol = Solution()
    ans = sol.convert('LEETCODEISHIRING',numRows=3)
    print(ans)