def PalinArray(arr ,n):
        N = int(input())
        array =[]
        for j in range(N):
            array.append(int(input()))
        for j in range(N):
            temp=int(array[j])
            p=0
            temp1=0
            while temp != 0:
                temp1= temp%10
                p=p*10+temp1
                temp=int(temp/10)
            if array[j] != p:
                return print(0)
        return print(1)
    
if __name__ == '__main__':
    n = int(input())
    arr =[]
    for i in range(n):
        PalinArray(arr,n)