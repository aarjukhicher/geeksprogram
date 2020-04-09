t= int(input())
for i in range(t):
    a=[]
    b=[]
    n=3 # number of skills
    result1=0
    result2=0
    for j in range(n):
        a.append(int(input()))
    for j in range(n):
        b.append(int(input()))
    while n>0:
        if a[n-1]>b[n-1]:
            result1 +=1
        elif a[n-1]<b[n-1]:
            result2 +=1
        else:
            pass
        n = n-1
    print(result1 ,result2)