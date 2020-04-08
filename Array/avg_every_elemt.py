t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    avg=0
    add=0
    for j in range(n):
        a.append(int(input()))
    for j in range(n):
        add=add+a[j]
        avg=int(add/(j+1))
        print(avg)