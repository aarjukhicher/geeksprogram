class Matrix:
    def __init__(self):
        self.a_matrix = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            for c in range(col):
                print("r ",r," c ",c,end=" ")
                temp.append(int(input()))
            self.a_matrix.append(temp)
    def printmatrrix(self,row,col):
        print()
        for r in range(row):
            print(self.a_matrix[r])
    def sumdiagonals(self,row,col):
        print()
        dia_sum1 = 0
        dia_sum2 = 0
        for r in range(row):
            for c in range(col):
                if r == c :
                    dia_sum1 = dia_sum1 + self.a_matrix[r][c]
                    if r+c == col-1:
                        dia_sum2 = dia_sum2 + self.a_matrix[r][c]
                elif r+c == col-1 :
                    dia_sum2 = dia_sum2 + self.a_matrix[r][c]
                else:
                    pass
        print("diagonal sum ",dia_sum1,"  ",dia_sum2)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.printmatrrix(row,col)
        m.sumdiagonals(row,col)