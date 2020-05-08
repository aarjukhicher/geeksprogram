def tripletfamily(array,n):
    for j in range(n-2):
        for k in range(n-1):
            k = j+1
            l = k+1
            while(l<n):
                if array[j]+array[k] > array[l]:
                    break
                elif array[j] + array[k] == array[l]:
                    print(1)
                    return
                l = l+1
    print(-1)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        array.sort()
        print(array)
        tripletfamily(array,n)