t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    temp=0
    k=int(input("number should be less than n "))
    for j in range(n):
        a.append(int(input()))
    temp=a[k-1]
    a[k-1]=a[n-k]
    a[n-k]=temp
    print(a)