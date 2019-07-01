"""
Given a matrix, rotate it right by 90 degrees in-place (ie with O(1) extra space)

Date: 28/06/19
Time Complexity: O(n^2)
Time taken: 30 min
"""
from utils.matrix import create_seq_matrix, print_matrix


def transpose_matrix(mat):
    """
    Rotate a matrix by 90 degrees to right.
    Ex:
    Original:
        1	2	3	4
        5	6	7	8
        9	10	11	12
        13	14	15	16


    Rotated:
        13	9	5	1
        14	10	6	2
        15	11	7	3
        16	12	8	4

    :param mat: Matrix to be rotated
    :return: transpose of matrix
    """
    rows = len(mat)
    for col in range(0, int(rows / 2)):
        for i in range(col, rows - col - 1):
            temp = mat[rows - i - 1][col]
            mat[rows - i - 1][col] = mat[rows - col - 1][rows - i - 1]
            mat[rows - col - 1][rows - i - 1] = mat[i][rows - col - 1]
            mat[i][rows - col - 1] = mat[col][i]
            mat[col][i] = temp
    return mat


matrix = create_seq_matrix(4)
print_matrix(matrix)
matrix = transpose_matrix(matrix)
print_matrix(matrix)
