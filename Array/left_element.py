t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for j in range(n):
        a.append(int(input()))
    temp=0
    for j in range(n):
        for k in range(j):
            if a[j]<a[k]:
                temp=a[j]
                a[j]=a[k]
                a[k]=temp
            else:
                pass
    index=int(len(a)/2)
    if index %2==0:
        print(a[index-1])
    else:
        print(a[index])
