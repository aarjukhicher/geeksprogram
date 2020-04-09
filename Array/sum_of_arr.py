t= int(input())
for i in range(t):
    n=int(input())
    a = []
    add =0
    for j in range(n):
        a.append(input())
    print(a)
    for j in range(n):
        add=add+int(a[j])
    print(add)