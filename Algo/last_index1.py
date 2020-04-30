def lastindex(a):
    count = -1
    len_a = len(a)
    temp = int(a)
    while len_a > 0:
        if temp % 10 == 1:
            count = count + len_a
            print(count)
            return
        len_a -= 1
        temp = temp/10
    print(count)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        a = input("only 0 & 1 ")
        lastindex(a)