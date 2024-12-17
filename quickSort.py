"""

类似递归版树的前序遍历，所有排序操作前置完成，而后重复左右区间的操作。

1. 递归的出口，指针法就是最小为1个数。
2. 递归的入口，一次排序后，标兵的位置已确定，该位置不用递归。
3. 用原地交换可以减少堆栈调用时的空间复杂度。
4. 标兵可以用random，随机选取，可以处理某些极端case。
5. 注意下等号，没有等号[13,2,4,5,9,13,0,23,8]，重复标兵会卡死。
"""

def quickSort(l,r):
    # 递归出口
    if r-l <= 0:
        return
    left,right = l,r
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] > pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    quickSort(left,l-1)
    quickSort(l+1,right)

if __name__ == "__main__":
    nums = [13,2,4,5,9,13,0,23,8]
    quickSort(0,len(nums)-1)
    print(nums)




