# ******************************************************************Arrays******************************************************************
# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def besttime(p):
    ans=0
    buy=p[0]
    for s in range(1,len(p)):
        if buy>p[s]:
            buy=p[s]
        profit=p[s]-buy
        ans=max(ans,profit)
    return ans
   
p=[7,1,5,3,6,4]
# print(besttime(p))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
def duplicate(n):
    # ol=len(n)
    # di=set(n)             ----method1-----
    # dil=len(di)
    # return dil!=ol
    dis=[]
    for i in n:
        if i in dis:
            return True
        dis.append(i)
    return False


n=[1,2,3,1]
# print(duplicate(n))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 238. Product of Array Except Self




def product(nums):
    n=len(nums)
    ans=[1]*n
    pre=1
    for i in range(n):
        ans[i]=pre
        pre*=nums[i]

    suf=1
    for i in range(n-1,-1,-1):
        ans[i]*=suf
        suf*=nums[i]
    return ans
        
    

nums=[1,2,3,4]
print(product(nums))

