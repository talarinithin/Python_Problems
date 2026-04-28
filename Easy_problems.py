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
    



    


arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3 
print(reversegroup(arr,k))
