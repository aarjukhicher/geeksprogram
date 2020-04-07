T =int(input())
for i in range(T):
    N = int(input())
    A = []
    for i in range(N):
        temp = input()
        A.append(temp)
    print(A)
    le =len(A)-1
    for j in range(int(N/2)):
        temp1 = A[j]
        A[j]=A[le]
        A[le]=temp1
        le=le-1
    print(A)