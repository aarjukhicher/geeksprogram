def printAl(arr,n):
    # your code here
    t = int(input())
    for i in range(t):
        n = int(input())
        for i in range(n):
            temp = input()
            if i%2 == 0:
                arr.append(temp)
        print(arr)
if __name__ == '__main__':
    arr =[]
    n=0
    print(printAl(arr,n))
