def sortarray(array,n):
    last = n-1
    first = 0
    temp = 0
    while first < last:
        if array[first] > array[last]:
            print("first and last ",first,last)
            temp = array[first]
            array[first] = array[last]
            array[last] = temp
            first += 1
        elif array[first] == 0:
            print("first ",first)
            first += 1
        else:
            print("last ",last)
            last -= 1
    print(array)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("only 0 & 1 ")))
        sortarray(array,n)
