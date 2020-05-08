def partsort(array,a,b,n):
    test = []
    for j in range(b+1):
        if j >= a:
            test.append(array[j])
    for j in range(len(test)-1):
        k = 0
        while(k < len(test)-1):
                if test[k] > test[k+1]:
                    temp = test[k]
                    test[k] = test[k+1]
                    test[k+1] = temp
                k = k+1
    for j in range(n):
        if j >=a and j <= b:
            array[j] = test.pop(0)
    print(array)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        a =int(input("a "))
        b =int(input("b "))
        partsort(array,a,b,n)