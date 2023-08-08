def square_matrix_simple(matrix[]):
    for row in enumerate(matrix):
        for col_index, element in enumerate(row):
            element  **= 2
            if col_index != 0:
                print(" ", end = "")
            print("{:d}".format(element), end = "")
        print()
    print(matrix)
