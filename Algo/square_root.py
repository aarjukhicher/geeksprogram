def squareroot(x):
    sqrt = 0
    sqrt = int(pow(x,1/2))
    print(sqrt)
    
if __name__=="__main__":
    t = int(input("test case "))
    for i in range(t):
        x = int(input("number "))
        squareroot(x)
