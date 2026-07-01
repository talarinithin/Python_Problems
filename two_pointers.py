# Two Pointer Technique
# 👉 Two pointers means using two variables (indexes) to traverse an array/string.

# Instead of using nested loops (O(n²)), we use two pointers → O(n).

# Basic idea:
# One pointer at start → left
# One pointer at end → right
# Move them based on condition
# 2. When to Use Two Pointers?

# Use this technique when:

# Array is sorted
# Need to find pairs / triplets
# Working with subarrays / substrings
# Need optimal (O(n)) solution

# 1. Two Sum II (LeetCode 167)
# Example 1
# Input:
# numbers = [2, 7, 11, 15]
# target = 9

def twosum(arr,t):
    l=0
    r=len(arr)-1

    while l<r:
        sumval=arr[l]+arr[r]
        if sumval==t:
            return [arr[l],arr[r]]
        elif sumval>t:
            r-=1
        else:
            l+=1
    return []
        



# arr=[2,7,11,15]
# t=9
# print(twosum(arr,t))


# 2. Remove Duplicates from Sorted Array (LeetCode 26)

def remove(arr):
    first=0
    for second in range(1,len(arr)):
        if arr[first]!=arr[second]:
            first+=1
            arr[first]=arr[second]
    return arr
  


# arr=[0,0,1,1,1,2,2,3,3,4]
# k=remove(arr)
# print(k)
# print(arr[:k])



# Valid Palindrome
def palindrome(s):
    l=0
    r=len(s)-1
    ans=True
    while l<r:
        if s[l]!=s[r]:
            ans=False
            break
        l+=1
        r-=1
    return ans


s='madam'
print(palindrome(s))



# Squares of a Sorted Array
def squre(n):
    l=0
    r=len(n)-1
    le=len(n)
    ans=[0]*le
    pos=len(n)-1
    while l<r:
        if abs(n[l])>abs(n[r]):
            ans[pos]=n[l]**2
            l+=1
        elif abs(n[l])<abs(n[r]):
            ans[pos]=n[r]**2
            r-=1
        pos-=1
    return ans


n=[-4, -1, 0, 3, 10]
print(squre(n))



# 283. Move Zeroes


def zeros(n):
    pos=0
    for i in range(len(n)):
        if n[i]!=0:
            n[i],n[pos]=n[pos],n[i]
            pos+=1
    return n
    

n=[0,1,0,3,12]
print(zeros(n))



# 167. Two Sum II - Input Array Is Sorted

def twosum(nums,t):
    l=0
    r=len(nums)-1
    while l<r:
        sumval=nums[l]+nums[r]
        if sumval==t:
            return [l+1,r+1]
        elif sumval<t:
            l+=1
        else:
            r-=1
    return

        
        

nums=[2,7,11,15]
t=9
print(twosum(nums,t))

#########------------15. 3Sum

def three(num):
    num.sort()
    res=set()
    for i in range(len(num)-2):
        l=i+1
        r=len(num)-1
        while l<r:
            tot=num[i]+num[l]+num[r]
            if tot==0:
                res.add((num[i],num[l],num[r]))
                l+=1
                r-=1
            elif tot<0:
                l+=1
            else:
                r-=1
    return [list(x) for x in res]






num=[-1,0,1,2,-1,-4]
print(three(num))




# --------------------75. Sort Colors-----------

#############---------METHOD1-----------###########

def sortcol(nums):
    pos=0
    for i in range(len(nums)):
        if nums[i]==0:
            nums[i],nums[pos]=nums[pos],nums[i]
            pos+=1
    lspos=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==2:
            nums[lspos],nums[i]=nums[i],nums[lspos]
            lspos-=1
    return nums

nums=[2,0,2,1,1,0]
print(sortcol(nums))



#############---------METHOD2-----------###########
def sortcolors(nums):
    low=0
    mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[low]==0:
            nums[low],nums[mid]==nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

nums=[2,0,2,1,1,0]
print(sortcolors(nums))



# -------------------11. Container With Most Water-----------
def water(height):
    l=0
    r=len(height)-1
    curr_area=0
    max_area=0
    while l<r:
        width=r-l
        curr_area=width*min(height[l],height[r])
        max_area=max(max_area,curr_area)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_area


height=[1,8,6,2,5,4,8,3,7]
print(water(height))




def boat(nums,li):
    nums.sort()
    # sumval=0
    # count=0
    # for i in range(len(nums)):
    #     sumval+=nums[i]
    #     if sumval>=2 and sumval<=li:
    #         count+=1
    #         sumval=0 
    # return count
    l=0
    r=len(nums)-1
    boats=0
    while l<=r:
        



nums=[3,2,2,1]
li=3
print(boat(nums,li))