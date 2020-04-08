t= int(input())
for i in range(t):
    n=int(input())
    a=[]
    multi=1
    for j in range(n):
        a.append(int(input()))
    for j in range(n):
        multi=multi*a[j]
    print(multi)