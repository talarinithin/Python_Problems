# Second Largest Element in an Array
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element.
def second(arr):
    first=0
    second=0
    for i in range(len(arr)):
        if arr[i]>first:
            first=arr[i]
    for i in range(len(arr)):
        if arr[i]>second and arr[i]!=first:
            second=arr[i]
    return second if second!=0 else -1


# arr=[12, 35, 1, 10, 34, 1]
# print(second(arr))



# Third largest element in an array

# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.

# Input: arr[] = [10, 2]
# Output: -1
# Explanation: There are less than three elements in the array, so the third largest element cannot be determined.

# Input: arr[] = [5, 5, 5]
# Output: 5
# Explanation: In the array [5, 5, 5], the third largest element can be considered 5, as there are no other distinct elements.

def third(arr):
    first=0
    second=0
    third=0
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and first!=second:
            second=arr[i]
    for i in range(len(arr)):
        if arr[i]>third and first!=arr[i] and second!=arr[i]:
            third=arr[i]

    return third


# Array Reverse


# arr=[2,4,1,3,5]
# print(third(arr))

# Input: arr[] = [1, 4, 3, 2, 6, 5]  
# Output:  [5, 6, 2, 3, 4, 1]
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = [4, 5, 1, 2]
# Output: [2, 1, 5, 4]
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

def reverse(arr):
    return arr[::-1]


def reverse(arr):
    left=0
    right=len(arr)-1

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    return arr


# arr=[4, 5, 1, 2]
# print(reverse(arr))

# Reverse an Array in groups
def reversegroup(arr,k):
    ans=[]
    for i in range(0,len(arr),k):
        group=arr[i:i+k]
        ans.extend(group[::-1])
    return ans
    



    


# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 3 
# print(reversegroup(arr,k))


# 1929. Concatenation of Array
def concatennation(nums):
    return nums+nums

# nums = [1,2,1]
# print(concatennation(nums))


# 1470. Shuffle the Array
# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:

# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:

# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]


def shuffle(nums,n):
    ans=[]
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans

    

# nums=[1,1,2,2]
# n=2
# print(shuffle(nums,n))


def minimum(n1,n2):
    # n=n1+n2
    # di={}
    # ans=[]
    # for i in n:
    #     di[i]=di.get(i,0)+1
    # for i,j in di.items():
    #     if j>=2:
    #         ans.append(i)
    ans=[]
    
    if len(ans)==0:
        return -1
    else:
        return min(ans)
       

n1=[1,2,3,6]
n2=[2,3,4,5]
# print(minimum(n1,n2))



# **********************************************************************************************************
# Find the Largest Element
def large(n):
    ans=0
    for i in n:
        if ans<i:
            ans=i
    return ans

def method2(n):
    l=n.sort()
    return n[-1]


n=[10, 25, 8, 45, 12]
print(large(n))
print(method2(n))


# -----------------------Find the Smallest Element------------
def small(n):
    ans=float('inf')
    for i in n:
        if ans>i:
            ans=i
    return ans

def sm2(n):
    n.sort()
    return n[0]


n=[12, 5, 18, 2, 9, 20]
print(small(n))
print(sm2(n))

# ----------------------------Find the Sum of Elements---------------------
def sumelem(n):
    ans=0
    for i in n:
        ans+=i
    return ans

def sum2(n):
    return sum(n)

n=[2,4,6,8,10]
print(sumelem(n))
print(sum2(n))

# ------------------------------Find the Average----------------------------
def avgval(n):
    return sum(n)/len(n)

def avg2(n):
    ans=0
    count=0
    for i in n:
        ans+=i
        count+=1
    return ans/count



n=[10,20,30,40]
print(avgval(n))
print(avg2(n))


# ---------------------------------------Count Even and Odd Numbers-----------------
def EOD(n):
    even=0
    odd=0
    for i in n:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

n=[1,2,3,4,5,6]
print(EOD(n))


# ------------------------------------------Reverse an Array------------------------------------
def revarray(n):
    return n[::-1]

def rev2(n):
    ans=[]
    for i in range(-1,-len(n)-1,-1):
        ans.append(n[i])
    return ans


n=[1,2,3,4,5]
print(revarray(n))
print(rev2(n))


# ---------------------------------Find the Second Largest Element---------------------
def seclar(n):
    sec=float('-inf')
    fir=float('-inf')
    for i in n:
        if fir<i:
            fir=i
    for j in n:
        if sec<j and j!=fir:
            sec=j
    return sec
    
    

n=[12, 45, 67, 23, 89, 56]
print(seclar(n))


# ---------------------------------Find the Maximum and Minimum---------------------------
def maxmin(n):
    return max(n),min(n)

def maxmin2(n):
    high=float('-inf')
    low=float('inf')
    for i in n:
        if high<i:
            high=i
    for j in n:
        if low>j:
            low=j
    return high,low

n=[8,15,2,19,10]
print(maxmin(n))
print(maxmin2(n))


# ------------------------------Search an Element--------------------------
def search(n,t):
    if t in n:
        return "found"
    


n=[10,20,30,40,50]
t=30
print(search(n,t))

# -------------------------------Count Frequency of an Element-------------------
def cou(n,t):
    count=0
    for i in n:
        if i==t:
            count+=1
    return count

def has(n,t):
    dic={}
    for i in n:
        dic[i]=dic.get(i,0)+1
    return dic.get(t,0)
    
    
    

n=[2, 5, 2, 8, 2, 9, 5]
t=2
print(cou(n,t))
print(has(n,t))