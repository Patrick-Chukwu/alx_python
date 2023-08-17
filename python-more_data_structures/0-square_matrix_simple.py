
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the squared values
        squared_row = []
        
        # Iterate through each element in the current row
        for element in row:
            # Square the element and add it to the squared row
            squared_row.append(element ** 2)
        
        # Add the squared row to the squared matrix
        squared_matrix.append(squared_row)

    for row in squared_matrix:
      print(row)
    return squared_matrix
    # Print the squared matrix
    

