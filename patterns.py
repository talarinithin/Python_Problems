def prblm1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()

prblm1(5)

print("-"*60)

def prblm2(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end=' ')
        print()
prblm2(5)

print("-"*60)

def prblm3(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end=' ')
        print()

prblm3(5)

print("-"*60)

def prblm4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

prblm4(5)

print('-'*60)

def prblm5(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=' ')
        print()

prblm5(5)

print('-'*60)

def prblm6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()

prblm6(5)

print('-'*60)

def prblm7(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end=" ")
        for j in range(2*i-1):
            print("*",end=' ')
        print()

prblm7(5)

print("-"*60)
def prblm8(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print(" ",end=" ")
        for j in range(2*n-2*i+1):
            print("*",end=' ')
        print()

prblm8(5)

print("-"*60)

def prblm9(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(2*i-1):
            print("*",end=' ')
        print()
    for i in range(1,n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(2*n-2*i-1):
            print("*",end=" ")
        print()

prblm9(5)


print("-"*60)

def prblm10(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==n or j==1:
                print("*",end=' ')
            else:
                print(" ",end=" ")
        print()

prblm10(5)


print("-"*60)

def prblm11(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i==5 or j==1 or i==j:
                print("*",end=' ')
            else:
                print(" ",end=" ")
        print()

prblm11(5)

print("*"*60)

#Floyd's triangle
def prblm12(n):
    num=1
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

prblm12(4)
print("*"*60)

def prblm13(n,m):
    for i in range(n):
        for j in range(m):
            print("*",end=" ")
        print()

prblm13(3,5)


print("*"*60)

def prblm14(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 or j==m or i==n or j==1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

prblm14(3,5)