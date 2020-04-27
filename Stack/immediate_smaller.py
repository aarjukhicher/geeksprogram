def imsmaller():
    k = 0
    len_stack = len(stack)-1
    while(k < len_stack):
        if stack[k] > stack[k+1]:
            print(stack[k+1])
        else:
            print(-1)
        k += 1
    print(-1)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        stack = []
        n = int(input("n "))
        for i in range(n):
            stack.append(input("input "))
        print(stack)
        imsmaller()