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
    def sumtriangle(self,row,col):
        print()
        tri1 = 0
        tri2 = 0
        for r in range(row):
            for c in range(col):
                if r == c or r*2 < r+c :
                    tri1 = tri1 + self.a_matrix[r][c]
                    if r == c :
                        tri2 = tri2 + self.a_matrix[r][c]
                elif r*2 > r+c :
                    tri2 = tri2 + self.a_matrix[r][c]
        print("diagonal sum ",tri1,"  ",tri2)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.printmatrrix(row,col)
        m.sumtriangle(row,col)