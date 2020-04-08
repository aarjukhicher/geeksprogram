t =int(input())
for i in range(t):
    n=int(input())
    arr=[]
    large1=0
    large2=0
    for j in range(n):
        arr.append(int(input()))
    for j in range(n):
        if large1>arr[j] and large2<=arr[j]:
            large2=arr[j]
        elif large1<arr[j]:
            large2=large1
            large1=arr[j]
    for j in range(n):
        if large1==arr[j] or large2==arr[j]:
            pass
        else:
            print(arr[j], end=" ")