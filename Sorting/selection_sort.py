def selectionsort(array,n):
    for j in range(n):
        k = j
        min = k
        while k < n :
            if array[min] > array[k]:
                min = k
            k = k+1
        temp = array[min]
        array[min] = array[j]
        array[j] = temp
    print("selection ",array)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        print(array)
        selectionsort(array,n)