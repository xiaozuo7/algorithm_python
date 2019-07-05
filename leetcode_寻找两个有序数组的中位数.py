# -*- coding: utf-8 -*-
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
 关键词： 递归,二分,二叉树,极限
时间复杂度为 O(log(m + n))
@author: xiaozuo
"""
#       left_A             |        right_A
# A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
#          i                           m-i

#       left_B             |        right_B
# B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
#          j                           n-j

#       left_part          |        right_part
# A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
# B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
#         i+j                        m-i + n-j

def median(A, B):
    # m ,n为两个数组的长度
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    # n是较大的那个数组的长度
    if n == 0:
        raise ValueError

    # [0, m]区间进行查找
    imin, imax = 0, m
    # 本来 i+j = m-i + n-j
    # 如果n>=m了就n数组比m数组长 那就在n-j那一部分+1  于是： i+j = m-i + n-j+1
    # 于是化简得到 j = (m+n+1)/2
    half_len =int((m + n + 1) / 2)  # 注意要整形,不然没办法查找 注意int(5/2)=2
    while imin <= imax:
        i = int((imin + imax) / 2)
        j = half_len - i
        # i>m right就为负了
        if i < m and B[j-1] > A[i]:
            # 说明A[i]太小了
            imin = i + 1
        # i<0 更不可能...
        elif i > 0 and A[i-1] > B[j]:
            # 说明A[i-1]太大了
            imax = i - 1
        else:
            # 这个时候第一个条件就完成了 进入到第二个条件
            # 极限思想去考虑边界情况
            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            # 这个是一般情况 二选一
            else:
                max_of_left = max(A[i-1], B[j-1])
            # 如果是奇数的话 直接返回就行了
            if (m + n) % 2 == 1:
                return max_of_left
            # 偶数的话右边也要算
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    A = [1, 2]
    B = [3, 4]
    ans = median(A, B)
    print(ans)