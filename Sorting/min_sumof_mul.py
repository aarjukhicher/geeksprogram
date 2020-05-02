def minsum_mul(array1,array2,n):
    temp = 0
    for j in range(n):
        temp += array1[j]*array2[j]
    print(temp)
t = int(input("t "))
for i in range(t):
    array1 = []
    array2 = []
    n = int(input("n "))
    for j in range(n):
        array1.append(int(input("array1 ")))
        array2.append(int(input("array2 ")))
    array1.sort()
    array2.sort(reverse= True)
    print("array1 ",array1)
    print("array2 ",array2)
    minsum_mul(array1,array2,n)