def appearonce(n,llist):
    temp = 0
    same = -1
    while temp < n :
        if llist[temp] == llist[temp+1]:
            same = llist[temp]
            temp += 2
        elif llist[temp] != same:
            same = llist[temp]
            if same != llist[temp+1]:
                print(same)
                return
            else:
                temp += 1
        else:
            temp += 1
    print(same)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        n = int(input("n "))
        llist = []
        for j in range(n):
            llist.append(int(input("input ")))
        llist.append(-1)
        appearonce(n,llist)