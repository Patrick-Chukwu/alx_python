# def print_matrix_integer(matrix=[[]]):
#     for x, y, z in matrix:
#         print("{:d} {:d} {:d}".format(x, y, z))


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, element in enumerate(row):
            if col_idx != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()