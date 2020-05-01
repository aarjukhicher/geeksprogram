def internship(array,key):
    temp = array
    item = 1
    while len(temp)>= key:
        len_arr = len(temp) - 1
        x =key-1
        temp1 =[]
        while x <= len_arr:
            temp1.append(temp[x])
            x = x + key
        print("temp1 ",temp1)
        temp = temp1

    item = temp[0]
    print("item ",item)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        n = int(input("n "))
        array = []
        key = int(input("key "))
        for j in range(n):
             array.append(j+1)
        print(array)
        internship(array,key)