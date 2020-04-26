def binaryqu(n):
    binary = []
    for i in range(n):
        temp = int(i+1)
        rem = 0
        num = 0
        temp1 = 1
        while(temp!=0):
            rem=temp%2
            temp = int(temp/2)
            num = num + rem*temp1
            temp1 = temp1*10
        binary.append(num)
    print("queue is ",binary)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        binaryqu(int(input("n ")))