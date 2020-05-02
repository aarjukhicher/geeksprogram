class Matrix:
    def __init__(self):
        self.a_matrix = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            for c in range(col):
                temp.append(int(input("input ")))
            self.a_matrix.append(temp)
        print(self.a_matrix)
    def transpose(self,row,col):
        for r in range(row):
            for c in range(col):
                print(self.a_matrix[c][r],end=" ")
            print()
    def mulmatrix(self,row,col,m,m1):
        for r in range(row):
            for c in range(col):
                for r1 in range(row):
                    self.a_matrix[r][c] += m.a_matrix[r][r1] * m1.a_matrix[r1][c]
        print(self.a_matrix) 

if __name__=="__main__":
    m = Matrix()
    m1 = Matrix()
    m2 = Matrix()
    row = int(input("row "))
    col = int(input("col "))
    m.insertmatrix(row,col)
    m1.insertmatrix(row,col)
    m2.insertmatrix(row,col)
    m2.mulmatrix(row,col,m,m1)
