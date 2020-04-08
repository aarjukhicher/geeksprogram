t=int(int(input()))
for i in range(t):
    n=int(int(input()))
    a=[]
    for j in range(n):
        a.append(int(input()))
    temp="PERFECT"
    k=0
    j=n-1
    while j>k:
        if a[j] != a[k]:
            temp="NOT PERFECT"
            break
        else:
            pass
        j-=1
        k+=1
    print(temp)