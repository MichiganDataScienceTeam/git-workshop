def validate_matrix(matrix):
    """
    Validates if the input is a well-formed matrix (2D list with consistent row lengths).
    :param matrix: 2D list representing the matrix.
    :return: True if valid, raises ValueError otherwise.
    """
    # TODO: Person 4 - Implement matrix validation logic
    dim2 = len(matrix[0])

    for row in matrix:
        if type(row) != list or len(row) != dim2:
            raise ValueError('Invalid matrix')

    return True

def check_dimensions(matrix1, matrix2):
    """
    Checks if two matrices can be added or multiplied.
    :param matrix1: First matrix (2D list).
    :param matrix2: Second matrix (2D list).
    :return: True if dimensions are compatible, raises ValueError otherwise.
    """
    # TODO: Person 4 - Implement dimension check logic
    m1d1 = len(matrix1)
    m1d2 = len(matrix1[0])
    m2d1 = len(matrix2)
    m2d2 = len(matrix2[0])

    if (m1d1 == m2d1 and m1d2 == m2d2) or (m1d1 == m2d2):
        return True

    raise ValueError('Invalid Dimensions')

def identity_matrix(size):
    """
    Creates an identity matrix of the given size.
    :param size: The number of rows/columns for the identity matrix.
    :return: Identity matrix as a 2D list.
    """
    # TODO: Person 4 - Implement identity matrix creation
    nrows = size[0]
    ncols = size[1]

    out = [[0] * ncols for _ in nrows]

    for i in range(min(nrows, ncols)):
        out[i][i] = 1
    return out

def zero_matrix(rows, cols):
    """
    Creates a zero matrix with the given dimensions.
    :param rows: Number of rows.
    :param cols: Number of columns.
    :return: Zero matrix as a 2D list.
    """
    # TODO: Person 4 - Implement zero matrix creation
    out = [[0] * cols for _ in rows]

    return out

def minor(matrix, row, col):
    """
    Calculates the minor of a matrix by removing the specified row and column.
    :param matrix: 2D list representing the matrix.
    :param row: The row to remove.
    :param col: The column to remove.
    :return: The minor matrix as a 2D list.
    """
    # TODO: Person 3 & 4 - Implement minor calculation
    # Either code together or have one person code and the other review
    # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
    # If reviewing, leave comments on what you think can be improved
    pass

def cofactor(matrix):
    """
    Calculates the cofactor matrix of a given matrix.
    :param matrix: 2D list representing the matrix.
    :return: Cofactor matrix as a 2D list.
    """
    # TODO: Person 3 & Person 4 - Implement cofactor calculation
    # Either code together or have one person code and the other review
    # ...
    pass

