print("-"*30+"Array Leader"+"-"*30)
def ArrayLeader(n):
    ans=[]
    for i in range(len(n)):
        is_leader=True
        for j in range(i+1,len(n)):
            if n[i]<n[j]:
                is_leader=False
        if is_leader:
            ans.append(n[i])
            
    return ans



# ------------------------# ANOTHER METHOD-------------------
def Array(n):
    ans=[]
    max_right=float("-inf")
    for i in range(len(n)-1,-1,-1):
        if n[i]>=max_right:
            ans.append(n[i])
            max_right=n[i]
    return ans[::-1]


n=[16,17,4,3,5,2]
print(ArrayLeader(n))
print(Array(n))

print("-"*30+"Rotate Array"+"-"*30)


def Rotate(n,d):
    d=d%len(n)
    n[:]=n[d:]+n[:d]
    return n
    

n=[7, 3, 9, 1]
d=9
print(Rotate(n,d))


print("-"*30+"Check Sorted Array"+"-"*30)


def sortarray(n):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            return False
    return True

n=[90, 80, 100, 70, 40, 30]
print(sortarray(n))