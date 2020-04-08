t=int(input())
for i in range(t):
    n= int(input())
    x= int(input())
    a=[]
    larger=0
    smaller=0
    for j in range(n):
        a.append(int(input()))
    for j in range(n):
        if x < a[j]:
            smaller+=1
        elif x > a[j]:
            larger+=1
        else:
            larger+=1
            smaller+=1
    print(smaller ,larger )