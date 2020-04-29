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
        print(self.a_matrix)
    def transposematrix(self,row,col):
        temp = []
        for r in range(int(row)):
            for c in range(int(col)):
                temp.append(self.a_matrix[c][r])
        print(temp)
        for r in range(row):
            for c in range(col):
                self.a_matrix[r][c] = temp.pop(0)
            print(self.a_matrix[r])

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.transposematrix(row,col)
