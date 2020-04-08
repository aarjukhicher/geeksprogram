t = int(input())
for i in range(t):
    n=int(input())
    arr = []
    small=0
    large=0
    for j in range(n):
        arr.append(int(input()))
    for j in range(n):
        if small==0 and large==0:
            small=arr[j]
            large=arr[j]
        elif arr[j]>large:
            large=arr[j]
        elif arr[j]<small:
            small=arr[j]
    print(large,small)