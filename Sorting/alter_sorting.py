def altersort(array,n):
    temp = []
    k = 0
    temp = array
    while(k < n):
        key = 0
        if k %2 == 0:
            for j in range(len(temp)-1):
                if temp[j] < temp[j+1]:
                    key = j +1
        else:
            for j in range(len(temp)-1):
                if temp[j] > temp[j+1]:
                    key = j +1
        k = k+1
        print(temp.pop(key))

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
    altersort(array,n)