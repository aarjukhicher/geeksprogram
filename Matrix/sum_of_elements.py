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
    def sumelement(self,row,col):
        sum_matrix = 0
        for r in range(row):
            for c in range(col):
                sum_matrix = sum_matrix + self.a_matrix[r][c]
        print("sum of matrix ",sum_matrix)

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.sumelement(row,col)
        