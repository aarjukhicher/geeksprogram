def sumisx(array,n,x,j):
    first = 0
    last = n-1
    while first < last:
        if j == first or j == last:
            if j == first:
                first += 1
            else :
                last -= 1
        elif (array[first] + array[last]) == x:
            print("f ",first," l ",last," j ",j," ")
            print("f ",array[first]," l ",array[last]," x ",x)
            return 1
        elif array[first] + array[last] > x:
            last -= 1
        else:
            first += 1
    return 0
def triplatesum(array,n):
    print("array",array)
    print()
    for j in range(n):
        x = array[j] * -1
        print(sumisx(array,n,x,j))
        if sumisx(array,n,x,j) == 1:
            return 1

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        array.sort()
        triplatesum(array,n)
        