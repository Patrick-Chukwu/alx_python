def print_matrix_integer(matrix=[[]]):
    for x, y, z in matrix:
        print("{}, {}, {}".format(x, y, z))

print_matrix_integer([(1, 2, 3), (4, 5, 6), (7, 8, 9)])