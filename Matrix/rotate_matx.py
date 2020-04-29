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
    def rotatematrix(self,row,col):
        for r in range(row):
            for c in range(col):
                print(self.a_matrix[c][col-(r+1)],end=" ")
            print()

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.rotatematrix(row,col)
