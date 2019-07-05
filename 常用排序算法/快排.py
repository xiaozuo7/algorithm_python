# -*- coding: utf-8 -*-
"""
快排的思想：首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，
所有比它大的数都放到它后面，这个过程称为一趟快速排序。

百度百科给的算法：
一趟快速排序的算法是：
1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，
使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。
另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。



时间复杂度：不稳定 O(nlgn) 最好：O(nlogn) 最坏：O(n^2)
@author: xiaozuo
"""

def QuickSort(myList,start,end):
    if start < end:
        i,j = start,end
        # 设置基准数
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1
            myList[i] = myList[j]

            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        # 递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

if __name__ == '__main__':

    myList = [49,38,65,97,76,13,27,49]
    print("Quick Sort: ")
    QuickSort(myList,0,len(myList)-1)
    print(myList)

