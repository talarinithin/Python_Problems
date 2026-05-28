# Input: [1,2,3,4,5], target = 4
# Output: 3

def prblm1(nums,t):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==t:
            return mid
            break
        elif nums[mid]<t:
            l+=1
        else:
            r-=1
    return -1

# nums= [1,2,3,4,5]
# t = 4
# print(prblm1(nums,t))

# -----------------------------------------------------------------------------------------------------------------------------------------

# 2. Search Insert Position

# If target not found, return correct insert position.

# Example:

# Input: [1,3,5,6], target = 2
# Output: 1

def prblm2(nums,t):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==t:
            return mid
            break
        elif nums[mid]<t:
            l+=1
        else:
            r-=1
    return mid

# nums=[1,3,5,6]
# t=2
# print(prblm2(nums,t))

# --------------------------------------------------------------------------------------------------------------------# ----------------------------------------------------------# ----------------------------------------------------------# ----------------------------------------------------------

# 3. First and Last Position of Element

# Find starting and ending index of target.

# Example:

# Input: [5,7,7,8,8,10], target = 8
# Output: [3,4]

def prblm3(nums,t):
    l=0
    r=len(nums)-1
    while l<=r:
        if nums[l]==t and nums[r]==t:
            return [l,r]
        elif nums[l]<t:
            l+=1
        else:
            r-=1
    return -1
        

nums=[1,2,2,2,3,4]
t=2
print(prblm3(nums,t))
#  ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------

# 4. Find Minimum in Rotated Sorted Array

# Example:

# Input: [4,5,6,7,0,1,2]
# Output: 0

# note:
# while l <= r → use when searching for an exact element.
# while l < r → use when narrowing down to a final position/answer.



def prblm4(nums):
    l=0
    r=len(nums)-1
    while l<r:
        mid=(l+r)//2
        if nums[mid]>r:
            l=mid+1
        else:
            r=mid
    return nums[l]

nums=[7,8,9,10,1,2,3,4]
print(prblm4(nums))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Search in Rotated Sorted Array

# Example:

# Input: [4,5,6,7,0,1,2], target = 0
# Output: 4

def prblm5(nums,t):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==t:
            return mid
            break
        if nums[l]<=nums[mid]:
            if nums[l]<=t<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[mid]<t<=nums[r]:
                l=mid+1
            else: 
                r=mid-1
    return -1

         
nums=[4,5,6,7,0,1,2]
t=5
# print(prblm5(nums,t))




#  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Lower Bound Problem
# Question

# Given a sorted array nums of size n and an integer x,
# find the lower bound of x.

# The lower bound is the smallest index such that:

# nums[i]≥x

# If no such index exists, return n.

# You must solve the problem using binary search.

def lowerbound(nums,x):
    l=0
    r=len(nums)-1
    ans=len(nums)
    while l<=r:
        mid=(l+r)//2
        if nums[mid]>=x:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

nums=[1,2,2,3]
x=2
print(lowerbound(nums,x))

def lowerbound1(nums,x):
    l=0
    r=len(nums)-1
    ans=len(nums)
    while l<=r:
        mid=(l+r)//2
        if nums[mid]>=x:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans


nums = [1,2,4,4,5,6]
x = 4
print(lowerbound1(nums,x))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Upper Bound Problem
# Question

# Given a sorted array nums of size n and an integer x,
# find the upper bound of x.
# The upper bound is the smallest index such that:
# nums[i]>x
# If no such index exists, return n.
# You must solve the problem using binary search.

# Input:
# nums = [1,2,2,3,4]
# x = 2

# Output:
# 3

# Input:
# nums = [1,2,2,3,4]
# x = 2

# Output:
# 3
def upperbound(nums,x):
    l=0
    r=len(nums)-1
    ans=len(nums)
    while l<=r:
        mid=(l+r)//2
        if nums[mid]>x:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

nums = [3,5,8,15,19]
x = 9
print(upperbound(nums,x))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Search Insert Position
# Question

# Given a sorted array nums and a target value target,
# return the index if the target is found.

# If not found, return the index where it should be inserted
# to maintain sorted order.

# You must solve it using binary search.
# *******************TEST CASES*************
# Input:                  |Input:                       
# nums = [1,3,5,6]        |nums = [1,3,5,6]
# target = 2              |target = 5
#                         |
# Output:                 |Output:
# 1                       |2


# Input:                  | # Input:
# nums = [1,3,5,6]        | # nums = [1,3,5,6]
# target = 7              | # target = 0
#                         |
# Output:                 | # Output:
# 4                       | # 0

# Important Note
# Search Insert Position Rule
# If target not found,
# return l

# after binary search ends.

def insertpos(nums,t):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==t:
            return mid
        elif nums[mid]<t:
            l=mid+1
        else:
            r=mid-1
    return l
    
            

nums=[1,3,5,6]
t=7
print(insertpos(nums,t))


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
