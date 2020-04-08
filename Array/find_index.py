t=int(int(input()))
for i in range(t):
    n=int(input())
    a=[]
    
    for j in range(n):
        a.append(int(input()))
    key=int(input())
    j=n-1
    k=0
    while j>=k:
        if a[k] == key and a[j] ==key:
            break
        elif a[k]== key:
            j-=1
        elif a[j]==key:
            k+=1
        else:
            j-=1
            k+=1
    if a[j]==key:
        print(k,j)
    else:
        print(-1)
