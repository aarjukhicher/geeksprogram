def possibletri(array,n):
    for j in range(n):
        k = j
        min = k
        while k < n:
            if array[min] > array[k]:
                min = k
            k += 1
        temp = array[min]
        array[min] = array[j]
        array[j] = temp
    print(array)
    temp = 0
    for j in range(2,n):
        k = 0
        l = j-1
        while k < l:
            if array[k]+array[l]> array[j]:
                temp = temp+ (l-k)
                l = l-1
            else:
                k = k+1
    print(temp)
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        possibletri(array,n)