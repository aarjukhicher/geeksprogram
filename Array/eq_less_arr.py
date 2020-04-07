t=int(input())
for i in range(t):
    n=int(input())
    l=0
    a = []
    for j in range(n):
        a.append(input())
    x=int(input("less or equal "))
    for j in range(n):
        if int(a[j])<= x:
            l=l+1
    print("output",l)