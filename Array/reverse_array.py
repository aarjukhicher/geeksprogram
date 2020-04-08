t=int(input())
for i in range(t):
    n=int(input())
    arr=[]
    for j in range(n):
        arr.append(int(input()))
    temp=0
    j=n-1
    k=0
    while j>0 and k<j:
        temp=arr[j]
        arr[j]=arr[k]
        arr[k]=temp
        k+=1
        j-=1
    print(arr)