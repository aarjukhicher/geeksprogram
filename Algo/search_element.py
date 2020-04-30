def searchelement(n,key,array):
    first = 0
    last = n -1
    mid = -1
    while first < last:
        mid = int((last+first)/2)
        if array[mid] == key or array[last]== key:
            if array[mid] ==key:
                print(mid)
            else:
                print(last)
            return
        elif array[mid] > key:
            last = mid
        else:
            first = mid
    print(-1)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        n = int(input("n "))
        key = int(input("key "))
        array = []
        print("enter sorted array")
        for j in range(n):
            array.append(int(input("input ")))
        searchelement(n,key,array)