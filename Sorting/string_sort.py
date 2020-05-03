def stringsort(string):
    s_list = []
    for j in string:
        s_list.append(j)
    for j in range(len(s_list)):
        for k in range(len(s_list)-(j+1)):
            if s_list[k] > s_list[k+1]:
                temp = s_list[k]
                s_list[k] = s_list[k+1]
                s_list[k+1] = temp
    string = ""
    for j in range(len(s_list)):
        string = string + s_list[j]
    print(string)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        string = input("enter string ")
        stringsort(string)