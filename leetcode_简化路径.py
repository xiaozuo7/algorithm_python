# -*- coding: utf-8 -*-
"""
示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。

示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。

示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

示例 4：

输入："/a/./b/../../c/"
输出："/c"

示例 5：

输入："/a/../../b/../c//.//"
输出："/c"

示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"
思路： 用栈的思想, 如果遇到.. 就弹出栈顶
@author: xiaozuo
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for tmp in path:
            if tmp=="..":
                if stack:stack.pop()
            elif tmp and tmp!=".":
                stack.append(tmp)
        return "/"+"/".join(stack)

if __name__ == '__main__':
    sol=Solution()
    path = "/a//b////c/d//././/.."
    print(sol.simplifyPath(path))