t=int(input())
for i in range(t):
    n=int(input())
    lag=0
    second=0
    a=[]
    for j in range(n):
        a.append(int(input()))
    for j in range(n):
        if lag<=a[j]:
            second=lag
            lag=a[j]
        elif second<=a[j]:
            second=a[j]
        else:
            pass
    print(second)