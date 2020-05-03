
def bubblesort(array,n):
    for j in range(n):
        k = 0
        for k in range(n-(j+1)) :
            if array[k] > array[k+1] :
                temp = array[k]
                array[k] = array[k+1]
                array[k+1] = temp 
    print("bubble ",array)
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        array = []
        n = int(input("n "))
        for j in range(n):
            array.append(int(input("input ")))
        print(array)
        bubblesort(array,n)