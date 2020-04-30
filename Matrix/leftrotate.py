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
    def leftrotatematrix(self,row,col,k):
        rotate = 0
        while(k > rotate):
            temp = []
            for r in range(row):
                for c in range(col):
                    if c+1 !=col :
                        temp.append(self.a_matrix[r][c+1])
                    else:
                        temp.append(self.a_matrix[r][0])
                print("temp ",temp)
            for r in range(row):
                for c in range(col):
                    self.a_matrix[r][c] = temp.pop(0)
                print(self.a_matrix[r])
            rotate += 1

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        k = int(input("how many times do you want to rotate "))
        m.insertmatrix(row,col)
        m.leftrotatematrix(row,col,k)
