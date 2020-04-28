class Matrix:
    def __init__(self):
        self.a_matx = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            for c in range(col):
                print("r ",r,"c ",c,end=" ")
                temp.append(int(input("input ")))
            print(temp)
            self.a_matx.append(temp)
    
    def printmatrix(self,row,col):
        print()
        for r in range(row):
            print(self.a_matx[r])
    
    def addmatrix(self,row,col,mat1):
        for r in range(row):
            for c in range(col):
                self.a_matx[r][c]= self.a_matx[r][c]+mat1.a_matx[r][c]
            

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        m1 = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.printmatrix(row,col)
        m1.insertmatrix(row,col)
        m1.printmatrix(row,col)
        m.addmatrix(row,col,m1)
        m.printmatrix(row,col)
