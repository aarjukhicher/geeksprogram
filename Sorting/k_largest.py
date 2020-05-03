def klargest(array,n,k):
    for j in range(n):
        for l in range(n-(j+1)):
            if array[l] < array[l+1] :
                temp = array[l]
                array[l] = array[l+1]
                array[l+1] = temp
            l += 1
    print(array)
    print(array[:k])
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        k = int(input("k "))
        for j in range(n):
            array.append(int(input("input ")))

        klargest(array,n,k)