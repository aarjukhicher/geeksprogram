t = int(input())
for i in range(t):
    n = int(input())
    arr= []
    for j in range(n):
        arr.append(int(input()))
    largest=0
    for j in range(n):
        if arr[j]>= largest:
            largest = arr[j]
        else:
            pass
    print(largest)