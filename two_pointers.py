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
  

arr=[0,0,1,1,1,2,2,3,3,4]
k=remove(arr)
print(k)
print(arr[:k])