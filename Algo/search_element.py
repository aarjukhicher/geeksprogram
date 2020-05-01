def searchelement(n,key,array):
    first = 0
    last = n -1
    mid = -1
    while first <= last:
        mid = int((last+first)/2)
        if array[mid] == key or array[first]== key:
            if array[mid] == key:
                print(mid)
                return
            else:
                print(first)
                return
        elif array[mid] > key:
            last = mid - 1
        else:
            first = mid + 1
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