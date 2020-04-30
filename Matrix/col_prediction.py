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
    
    def colprediction(self,row,col):
        temp = []
        for c in range(col):
            temp.append(0)
        print(temp)
        for r in range(row):
            for c in range(col):
                if self.a_matrix[r][c] == 0:
                    temp[c] = temp[c] + 1
                else:
                    temp[c] = temp[c] + 0
        count = -1
        for c in range(col-1):
            if temp[c] > temp[c+1]:
                count = c
            elif temp[c] < temp[c+1]:
                count = c+1
        print(count)
    
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.colprediction(row,col)
