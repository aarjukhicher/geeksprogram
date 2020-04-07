t = int(input())
for i in range(t):
    n=int(input())
    a = []
    for j in range(n):
        a.append(input())
    temp=""
    for j in range(n):
        if len(a[j]) >= len(temp):
            temp = a[j]
        else:
            temp = temp
    print(temp)
