t= int(input())
for i in range(t):
    n=int(input())
    a = []
    sum =0
    for j in range(n):
        a.append(input())
    print(a)
    for j in range(n):
        sum=sum+int(a[j])
    print(sum)