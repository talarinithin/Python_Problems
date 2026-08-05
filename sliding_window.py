# Maximum Sum Subarray of Size K


def maxsum(arr,k):
    window=sum(arr[:k])
    ans=window
    for i in range(k,len(arr)):
        window+=arr[i]-arr[i-1]
        ans=max(ans,window)
    return ans

# arr = [5, 5, 5, 5]
# k = 2
# print(maxsum(arr,k))

def avgsub(arr,k):
    win=sum(arr[:k])
    ans=[win/k]
    for i in range(k,len(arr)):
        win+=arr[i]-arr[i-k]
        ans.append(win/k)
    return ans 
    

# arr = [2,4,6,8]
# k = 2
# print(avgsub(arr,k))




def max_wid(arr,k):
    ans=[]
    for i in range(len(arr)-k+1):
        ans.append(max(arr[i:k+i]))
    return ans


arr = [1,3,-1,-3,5,3,6,7]
k = 3
print(max_wid(arr,k))


def maxavg(nums,k):
    wid=sum(nums[:k])
    ans=[wid/k]
    for i in range(k,len(nums)):
        wid+=nums[i]-nums[i-k]
        ans.append(wid/k)
    return max(ans)
    

nums=[1,12,-5,-6,50,3]
k=4
print(maxavg(nums,k))

 

