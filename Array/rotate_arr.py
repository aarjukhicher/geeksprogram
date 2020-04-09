t=int(input("t "))
for i in range(t):
    n=int(input("n "))
    d=int(input("d "))
    a=[]
    for j in range(n):
        a.append(int(input()))
    temp=0
    while d>0:
        temp=a[0]
        a.remove(a[0])
        a.append(int(temp))
        print(a)
        d-=1
    