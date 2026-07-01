def leap(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return "leap year"
    else:
        return "not leap year"


n=int(input())
print(leap(n))