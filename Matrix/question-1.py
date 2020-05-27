class Matrix:
    def __init__(self):
        self.a_matrix = []
    def insertmatrix(self,row,col):
        for r in range(col):
            temp = []
            test = 0
            n=r+1
            if r%2==0:
                test =int(((n+1)/2)*n)
            else:
                test= int(((n/2)*n)+(n/2))
            for c in range(row):
                temp.append(test)
                test = test+prime[c]
            self.a_matrix.append(temp)
    def transposematrix(self,row,col):
        temp = []
        for r in range(int(row)):
            for c in range(int(col)):
                temp.append(self.a_matrix[c][r])
        # print(temp)
        for r in range(row):
            for c in range(col):
                self.a_matrix[r][c] = temp.pop(0)
            # print(self.a_matrix[r])

    def printmatrrix(self,row,col):
        for r in range(row):
            print(self.a_matrix[r])
    def primenumber(self,prime):
        r=70
        for p in range(2,r):  
            k=0  
            for i in range(2,p):  
                if(p%i==0):  
                    k=k+1  
            if(k<=0):  
                prime.append(p)

if __name__=="__main__":
        m = Matrix()
        row = 5
        col = 5
        prime=[]
        m.primenumber(prime)
        m.insertmatrix(row,col)
        m.transposematrix(row,col)
        m.printmatrrix(row,col)
        