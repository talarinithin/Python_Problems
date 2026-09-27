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