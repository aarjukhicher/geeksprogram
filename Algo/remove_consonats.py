def removeconsonat(string):
    temp = []
    substr = ['a','e','i','o','u']
    for i in string:
        temp.append(i)
    print(temp)
    for i in range(len(temp)):
        for j in range(len(substr)):
            if temp[i] == substr[j] or temp[i] == substr[j].upper() or temp[i] ==" ":
                print(temp[i],end="")

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        string = input("enter string : ")
    removeconsonat(string)