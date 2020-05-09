def megasale(array,n,key):
    profit = 0
    for j in range(n):
        k = j+1
        while(k < n):
            if array[j] > array[k]:
                temp = array[k]
                array[k] = array[j]
                array[j] = temp
            k = k+1
    for j in range(key):
        if array[j] < 0:
            profit = profit+array[j]
    print(profit*-1)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        key = int(input("key "))
        for j in range(n):
            array.append(int(input("input ")))
        megasale(array,n,key)