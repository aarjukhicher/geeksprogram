class Matrix:
    def __init__(self):
        self.a_matx = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            for c in range(col):
                print("R ",r,"C ",c,end=" ")
                temp.append(input("input "))
            print(temp)
            self.a_matx.append(temp)
   
    def printmatrix(self,row,col):
        print()
        for r in range(row):
            print(self.a_matx[r])

    def mulmatrix(self,row,col,mat,mat1):
        if row != col:
            print("Matrix in not mul ")
            return
        for r in range(row):
            for c in range(col):
                for c1 in range(row):
                    self.a_matx[r][c] = mat.a_matx[r][c1] + mat1.a_matx[c1][c]
                     

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        m1 = Matrix()
        m2 = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.printmatrix(row,col)
        m1.insertmatrix(row,col)
        m1.printmatrix(row,col)
        m2.insertmatrix(row,col)
        m2.printmatrix(row,col)
        m2.mulmatrix(row,col,m,m1)
        m2.printmatrix(row,col)
