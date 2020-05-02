def specificsorting(array,n):
    f = 0
    l = n-1
    temp = 0
    while f < l :
        if array[f]%2 == 0 :
            temp = array[f]
            array[f] = array[l]
            array[l] = temp
            l -= 1
        elif array[l]%2 == 1 :
            temp = array[l]
            array[l] = array[f]
            array[f] = temp
            f +=1
        else :
            f = f+1
            # l = l-1
    print("f ",f," l ",l)
    print(array)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        specificsorting(array,n)
