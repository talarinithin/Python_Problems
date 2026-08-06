#-------------- 3345. Smallest Divisible Digit Product I


# You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
# Example 1:
# Input: n = 10, t = 2
# Output: 10
# Explanation:
# The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

# Example 2:
# Input: n = 15, t = 3
# Output: 16
# Explanation:
# The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.


def smallDivsible(n,t):
    while True:
        temp=n
        product=1
        while temp!=0:
            product*=temp%10
            temp=temp//10
        if product%t==0:
            return n
        n+=1
        

n=15
t=3
print(smallDivsible(n,t))



# *****************************************************************************************************

# ---------------3731. Find Missing Elements

# You are given an integer array nums consisting of unique integers.

# Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

# The smallest and largest integers of the original range are still present in nums.

# Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.
# Example 1:
# Input: nums = [1,4,2,5]
# Output: [3]
# Explanation:
# The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. Among these, only 3 is missing.

# Example 2:
# Input: nums = [7,8,6,9]
# Output: []
# Explanation:
# The smallest integer is 6 and the largest is 9, so the full range is [6,7,8,9]. All integers are already present, so no integer is missing.

def findMissing(nums):
    a=[]
    for i in range(min(nums),max(nums)+1):
        a.append(i)
    b=set(nums)
    ans=[]
    for i in a:
        if i not in b:
            ans.append(i)
    return ans

nums=[5,1]
print(findMissing(nums))