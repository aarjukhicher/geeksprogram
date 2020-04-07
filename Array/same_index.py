t= int(input())
for i in range(t):
    n= int(input())
    a =[]
    for i in range(n):
        a.append(input())
    for j in range(n):
        if int(a[j])==j+1:
            print(j+1)
        else:
            pass
        