def sortpos(array,n,key):
    test = array[key]
    print("temp ",test)
    count = 0
    for j in range(key):
        if array[j] == test:
            count = count+1
    print("c ",count)
    for j in range(n):
        k = j+1
        while(k < n):
            if array[j] > array[k]:
                temp = array[k]
                array[k] = array[j]
                array[j] = temp
            k = k+1
    print(array)
    for l in range(n):
        print("l ",l," ",array[l])
        if array[l]==test:
            count = count + l
            break
    print(count)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        key = int(input("key "))
        for j in range(n):
            array.append(int(input("input ")))
        sortpos(array,n,key)