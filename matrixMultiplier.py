#The Matrix class acts as its own variable type, mimicing the math array
class Matrix:
    
    def __init__(self, name:str, rows:int, columns:int, elements):
        self.name = str(name[0].capitalize())
        self.rows = int(rows)
        self.columns = int(columns)
        self.elements = elements

    def edit(self, name, rows, columns, elements):
        self.name = str(name[0].capitalize())
        self.rows = int(rows)
        self.columns = int(columns)
        self.elements = elements

    def define(self):
        return f"{str(self.name)}({str(self.rows)}x{str(self.columns)})= {self.elements}"

# make the matrix
def makeMatrix(matrixName, rowVar, columnVar, elementList):
    row = 1
    while row <= rowVar:
        elementList.append([])
        column = 1
        while column <= columnVar:
            elementList[row - 1].append(int(input(f"Enter the element in row: {row} column: {column} of {matrixName}: ")))
            column += 1
        row += 1

    return matrixName, rowVar, columnVar, elementList

def multiply(m1, m2):
        if m1.columns != m2.rows:
            raise ValueError("Cannot multiply: Number of columns in the first matrix must equal the number of rows in the second matrix.")
        
        result = [[0 for _ in range(m2.columns)] for _ in range(m1.rows)]
        
        for i in range(m1.rows):
            for j in range(m2.columns):
                for k in range(m1.columns):
                    result[i][j] += m1.elements[i][k] * m2.elements[k][j]
        
        return result

def main():
    Matrix1 = Matrix(input("Enter the name of the Matrix: ")[0].capitalize(), 1, 1, [])
    Matrix2 = Matrix(input("Enter the name of the Matrix: ")[0].capitalize(), 1, 1, [])
    matrices = [Matrix1, Matrix2]

    for m in matrices:
        m.edit(*makeMatrix(m.name, int(input(f"Enter the amount of rows in {m.name}: ")), int(input(f"Enter the amount of columns in {m.name}: ")), m.elements))

    for m in matrices:
        print(f"{m.define()}")


    print(f"{Matrix1.name}{Matrix2.name}={multiply(Matrix1, Matrix2)}")

main()

if __name__ == '__main__':
    main()