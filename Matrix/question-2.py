class Matrix:
    def __init__(self):
        self.a_matrix = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            test = 0
            n=r+1
            if r%2==0:
                test =int(((n+1)/2)*n)
            else:
                test= int(((n/2)*n)+(n/2))
            for c in range(col):
                temp.append(test)
                test = test+prime[c]
            self.a_matrix.append(temp)
    def transposematrix(self,row,col):
        temp = []
        for r in range(int(row)):
            for c in range(int(col)):
                temp.append(self.a_matrix[c][r])
        
        for r in range(row):
            for c in range(col):
                self.a_matrix[r][c] = temp.pop(0)
            # print(self.a_matrix[r])

    def printmatrrix(self,row,col):
        for r in range(row):
            print(self.a_matrix[r])
    def primenumber(self,prime):
        r=72
        for p in range(2,r):  
            k=0  
            for i in range(2,p):  
                if(p%i==0):  
                    k=k+1  
            if(k<=0):  
                prime.append(p)
  
    def sortdiagonals(self,row,col):
        print()
        diagonal = []
        for r in range(row):
            for c in range(col):
                if r+c == col-1 :
                    diagonal.append(self.a_matrix[r][c])
                else:
                    pass
        for r in range(row):
            if diagonal[r]%2==0 :
                temp1 = diagonal[r]
                test1 = 0
                while(temp1 !=0):
                    rem = temp1 % 10
                    test1 = test1*10+rem
                    temp1 = int(temp1/10)
                diagonal[r]=test1
        diagonal.sort()
        print(diagonal)

if __name__=="__main__":
        m = Matrix()
        row = 20
        col = 20
        prime=[]
        m.primenumber(prime)
        m.insertmatrix(row,col)
        m.transposematrix(row,col)
        m.printmatrrix(row,col)
        m.sortdiagonals(row,col)
        