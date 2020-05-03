def insertarray(array,n):
    for j in range(n):
        array.append(int(input("input ")))
    print(array)
def countpairsum(array1,array2,n1,n2,x):
    count = 0
    for n in range(n1):
        m = n2 -1
        while m >= 0 :
            if array1[n]+array2[m] == x :
                count += 1
            elif array1[n]+array2[m] < x :
                break
            m = m-1
    print(count)
if __name__=="__main__":
    t =int(input("t "))
    for i in range(t):
        array1 = []
        array2 = []
        n1 = int(input("n1 "))
        n2 = int(input("n2 "))
        insertarray(array1,n1)
        insertarray(array2,n2)
        x = int(input("x "))
        countpairsum(array1,array2,n1,n2,x)
