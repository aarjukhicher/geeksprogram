def insertstack(string):
    stack = []
    for i in string:
        stack.append(i)
        print(stack)
    for i in string:
        print(stack.pop(), end="")

if __name__=="__main__":
    t = int(input("t "))
    for t in range(t):
        string = input("insert string ")
        insertstack(string)
    