# ------------1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

def prefix(nums):
    n=len(nums)
    pre=[0]*n
    pre[0]=nums[0]
    for i in range(1,n):
        pre[i]=pre[i-1]+nums[i]
    return pre


nums=[1,2,3,4]
# print(prefix(nums))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------724. Find Pivot Index
# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
def pivot(nums):
    tot=sum(nums)
    left=0
    for i in range(len(nums)):
        right=tot-left-nums[i]
        if left==right:
            return i
        left+=nums[i]
    return -1


def pivotpref(nums):
    n=len(nums)
    pre=[0]*n
    suf=[0]*n
    for i in range(1,n):
        pre[i]=pre[i-1]+nums[i-1]
    for i in range(n-2,-1,-1):
        suf[i]=suf[i+1]+nums[i+1]
    return suf

    # for i in range(n):
    #     if pre[i]==suf[i]:
    #         return i
    # return -1


nums=[1,7,3,6,5,6]
# print(pivotpref(nums))

#  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

def prefix(nums):
    n=len(nums)
    pre=[0]*n
    pre[0]=nums[0]
    for i in range(1,n):
        pre[i]=pre[i-1]+nums[i]
    return pre

def sumrange(pre,left,right):
    if left==0:
        return pre[right]
    return pre[right]-pre[left-1]

nums=[-2,0,3,-5,2,-1]

pre=prefix(nums)
print(sumrange(pre,0,2))
print(sumrange(pre,2,5))
