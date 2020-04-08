t =int(input())
for t in range(t):
    n=int(input())
    a =[]
    add=0
    for j in range(n):
        a.append(int(input()))
    for j in range(n):
        add=add+a[j]
    print(add)