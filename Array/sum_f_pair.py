t=int(input("t "))
for i in range(t):
    n=int(input("n "))
    a=[]
    result=0
    for j in range(n):
        a.append(int(input()))
    print()
    for l in range(n):
        for m in range(l+1,n):
            print("l m ",l ,m)
            if a[m]-a[l] > 1 :
                print("w ",a[m],a[l])
                result=result+(a[m]-a[l])
            elif a[m]-a[l] < -1:
                print("w ",a[m],a[l])
                result=result+(a[m]-a[l])
            else:
                print("w ",a[l],a[m])
                result=result
    print("r ",result)