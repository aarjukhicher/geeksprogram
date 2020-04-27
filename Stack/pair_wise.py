def checkpair():
    k = 0
    len_stack = len(stack)
    if len_stack%2 == 1 :
        stack.pop()
        len_stack = len(stack)
    while(k < len_stack):
        if (stack[k]+1) != stack[k+1]:
            print("NO")
            return
        else:
            pass
        k += 2
    print("YES")

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        stack = []
        n = int(input("n "))
        for j in range(n):
            stack.append(int(input("input ")))
        print(stack)
        checkpair()
