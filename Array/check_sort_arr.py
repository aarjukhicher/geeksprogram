t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for j in range(n):
        a.append(int(input()))
    k=1
    j=1
    while k==1 and j<n:
        if a[j]>=a[j-1]:
            pass
        else:
            k=0
        j+=1
    print(k)