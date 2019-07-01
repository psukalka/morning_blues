def print_matrix(mat):
    """
    Utility to print a two dimensional matrix
    :param mat:
    :return:
    """
    rows = len(mat)
    for row in range(0, rows):
        cols = len(mat[row])
        row_str = ""
        for col in range(0, cols):
            row_str += str(mat[row][col]) + "\t"
        print(row_str)
    print()


def create_zero_matrix(n):
    """
    Utility method to return empty nxn matrix
    :param n:
    :return:
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.insert(j, 0)
        matrix.insert(i, row)
    return matrix


def create_seq_matrix(n):
    """
    Utility to fill a matrix with values 1,2,3,... in sequence
    :param n:
    :return:
    """
    count = 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.insert(j, count)
            count += 1
        matrix.insert(i, row)
    return matrix
