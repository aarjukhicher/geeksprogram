t =int(input())
for i in range(t):
    n=int(input())
    coef=1
    
    for i in range(n):
        a=[]
        for j in range(i+1):
            if i ==0 or j==0:
                coef=1
            else:
                coef=int(coef*(i-j+1)/(j))
            a.append(int(coef))
        print(a)