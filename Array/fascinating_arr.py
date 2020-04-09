t=int(input())
for i in range(t):
    n=input("number should be 3 value ")
    f=1
    n2=int(n)*2
    n3=int(n)*3
    a=str(n2)+str(n3)
    print("a",a)
    for i in a:
        for j in n:
            if i==j:
                f=0
                break
            else:
                pass
    print(f)
    
    