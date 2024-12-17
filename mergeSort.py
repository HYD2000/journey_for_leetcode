"""

类似树的后序遍历，排序操作放在最后完成，其实是对最小单位先进行比较操作，由下而上合并完成

1. 还是要注意出口，边界是处理一个的情况。
2. 划分的位置，一般取中间，二分。
3. 递归是左右区间，合并是左右区间的两个有序数组合并成一个有序数组。
4. 最好是能实现原地排序，否则会多出O(N)的空间。
"""

def mergeSort(l,r):
    # 递归出口
    if r-l <= 0:
        return
    # 划分的位置
    mid = int((l+r)/2)
    # 先拆分区间，再合并数组，后置处理有序数组排序
    mergeSort(l,mid)
    mergeSort(mid+1,r)
    mergeV2(l,mid,r)

'''
TODO: 目前有额外O(n)空间，如何实现原地排序 
'''
def merge(l,mid,r):
    merged = []
    left,right = l,mid+1
    while left < mid+1 and right < r+1:
        if nums[left] > nums[right]:
            merged.append(nums[right])
            right += 1
        elif nums[left] <= nums[right]:
            merged.append(nums[left])
            left += 1
    while left < mid+1:
        merged.append(nums[left])
        left += 1
    while right < r+1:
        merged.append(nums[right])
        right += 1
    for i in range(r+1-l):
        nums[i+l] = merged[i]


"""
FIXED: GPT给的解法，还不错
"""
def mergeV2(l,mid,r):
    left,right = l,mid+1
    while left < mid+1 and right < r+1:
        # 右侧数组中的数较小
        if nums[left] > nums[right]:
            tmp = nums[right]
            idx = right
            # 需要按位置移动left前面的数，找到left位置插入，其实是插入排序
            while idx > left:
                nums[idx] = nums[idx-1]
                idx -= 1
            nums[left] = tmp
            right += 1
        else:
            left += 1


if __name__ == "__main__":
    nums = [13,2,4,5,9,13,0,23,8,-89,0]
    mergeSort(0,len(nums)-1)
    print(nums)




