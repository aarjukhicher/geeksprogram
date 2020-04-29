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
        print()
        print(self.a_matrix)
        print()
    def checkidentical(self,row,col,mat1):
        for r in range(row):
            for c in range(col):
                if self.a_matrix[r][c] != mat1.a_matrix[r][c]:
                    print("NO")
                    return
        print("YES")

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        m1 = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m1.insertmatrix(row,col)
        m.checkidentical(row,col,m1)
