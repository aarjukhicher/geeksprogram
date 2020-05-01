def doublingvalue(n,key,array):
    for j in range(n):
        if array[j] == key:
            key *= 2
    print(key)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        n = int(input("n "))
        array = []
        key = int(input("key "))
        for j in range(n):
            array.append(int(input("input ")))
        doublingvalue(n,key,array)