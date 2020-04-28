class Matrix:
    def __init__(self):
        self.a_matx = []
    def insertmatrix(self,row,col):
        for r in range(row):
            temp = []
            for c in range(col):
                print("r ",r,"c ",c,end=" ")
                temp.append(input("input "))
            print(temp)
            self.a_matx.append(temp)
    def printmatrix(self,row,col):
        print()
        for r in range(row):
            print(self.a_matx[r])

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        m = Matrix()
        row = int(input("row "))
        col = int(input("col "))
        m.insertmatrix(row,col)
        m.printmatrix(row,col)
