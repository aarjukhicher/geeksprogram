class Matrix:
    def __init__(self):
        self.a_matrix = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            for c in range(col):
                print("r ",r,"c ",c,end=" ")
                temp.append(input("input "))
            print(temp)
            self.a_matrix.append(temp)
    def snakematrix(self,row,col):
        for r in range(row):
            if r % 2 == 0:
                for c in range(col):
                    print(self.a_matrix[r][c],end=" ")
                print()
            else:
                c = col -1
                while(c >= 0):
                    print(self.a_matrix[r][c],end=" ")
                    c -= 1
                print() 

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.snakematrix(row,col)