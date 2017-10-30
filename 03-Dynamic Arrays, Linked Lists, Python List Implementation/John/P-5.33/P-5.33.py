#Solution to project P-5.33

class Matrix:

    def __init__(self, rows, columns):
        self.rows = int(rows)
        self.columns = int(columns)

        self.matrix_list = []
        #creates an empty matrix with dimensions rowsxcolumns
        for i in range(rows):
            row_list = []
            for j in range(columns):
                row_list.append(0.0)
            self.matrix_list.append(row_list)

    #prints each row in easy to read format
    def print_matrix(self):
        for row in self.matrix_list:
            print(str(row))

    #user prompt to manually input every value
    def populate_matrix(self):
        print('Input values at each position.')
        for row_index in range(len(self.matrix_list)):
            for column_index in range(self.columns):
                print('[' + str(row_index + 1) + ',' + str(column_index + 1) + ']: ', end='') #+1 because matrix notation starts at 1
                self.matrix_list[row_index][column_index] = float(input())

    def add_matrix(self, matrix_two):

        print()
        self.print_matrix()
        print('\n+\n')
        matrix_two.print_matrix()

        if (self.rows, self.columns) == (matrix_two.rows,matrix_two.columns):
            #print('Me Me Big Boy')
            return_matrix = Matrix(self.rows,self.columns)
            for row_index in range(len(self.matrix_list)):
                for column_index in range(self.columns):
                    return_matrix.matrix_list[row_index][column_index] = self.matrix_list[row_index][column_index] + matrix_two.matrix_list[row_index][column_index]
            return return_matrix
        else:
            print('Dimensions of A does not match dimensions of B')
            return self

    def multiply_matrix(self, matrix_two):

        print()
        self.print_matrix()
        print('\n*\n')
        matrix_two.print_matrix()

        if self.columns == matrix_two.rows:
            return_matrix = Matrix(self.rows,matrix_two.columns)
            for row_index in range(self.rows):
                for column_index in range(matrix_two.columns): #iterates once per every entry in return_matrix
                    value = 0
                    for inner_index in range(self.columns):
                        value += self.matrix_list[row_index][inner_index] * matrix_two.matrix_list[inner_index][column_index]
                    return_matrix.matrix_list[row_index][column_index] = value
            return return_matrix

        else:
            print('Dimensions just don\'t work out, dude')
            return self

matrix = Matrix(2,2)
matrix.populate_matrix()
matrix_two = Matrix(2,3)
matrix_two.populate_matrix()
multiplied_matrix = matrix.multiply_matrix(matrix_two)
print('\n----------------------------------------------\n')
multiplied_matrix.print_matrix()
