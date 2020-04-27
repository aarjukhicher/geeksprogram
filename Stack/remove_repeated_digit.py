t = int(input("t "))
for i in range(t):
    temp = 0
    digit = 0
    stack = []
    a = int(input("enter digit"))
    temp = a
    while(temp != 0):
        stack.append(temp % 10)
        temp = int(temp/10)
    print(stack)
    digit = stack[0]
    for j in range(len(stack)-1):
        if stack[j] != stack[j+1]:
            digit = digit*10+stack[j+1]
        else:
            pass
    print("digit: ",digit)