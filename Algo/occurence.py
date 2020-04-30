def occurence(n,key):
    count = 0
    for j in range(n):
        if key == llist[j]:
            count += 1
        elif key< llist[j]:
            print(count)
            return

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        n = int(input("n "))
        llist = []
        key = int(input("key "))
        for j in range(n):
            llist.append(int(input("input ")))
        occurence(n, key)