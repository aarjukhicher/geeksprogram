def maxproduct(array,n):
    for i in range(n-1):
        j = i+1
        minn = i
        while j < n-1: 
            if array[minn] > array[j]:
                minn = j
            j = j+1
        temp = array[i]
        array[i] = array[minn]
        array[minn] = temp
    print(array[n-1]*array[n-2])

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        maxproduct(array,n)