def countzero():
    count = 0
    arr_len = len(a)
    for k in range(arr_len):
        if a[k] == "0":
            count = arr_len - k
            print(count)
            return
        elif k == arr_len-1:
            print(count)
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        a = []
        n = int(input("n "))
        for j in range(n):
            a.append(input("input on 1 and 0 "))
    countzero()