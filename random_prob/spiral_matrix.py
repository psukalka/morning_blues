"""
Date: 27/06/19
Program to fill (and optionally print) a matrix with numbers from 1 to n^2 in spiral form.
Time taken: 24min
Time complexity: O(n^2)

*) Matrix formed with [[0]*n]*n will result in n copies of same list. Fill matrix elements individually instead.
"""
from utils.matrix import print_matrix


def fill_spiral(n):
    '''
    There are total four directions. Left to right (LR), Top to Bottom (TB), Right to left (RL) or Bottom to Top (BT).
    To fill a spiral matrix, we need to change directions at either boundary of the matrix or if the element is already filled.
    :param n: width of the box
    '''
    direction = "LR"
    start_x = 0
    start_y = -1
    count = 1
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.insert(j, 0)
        matrix.insert(i, row)
    while count <= n * n:
        if direction == "LR":
            i = start_x
            for j in range(start_y + 1, n):
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = count
                count += 1
                start_y = j
            direction = "TB"
        if direction == "RL":
            i = start_x
            for j in range(start_y - 1, -1, -1):
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = count
                count += 1
                start_y = j
            direction = "BT"
        if direction == "TB":
            j = start_y
            for i in range(start_x + 1, n):
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = count
                count += 1
                start_x = i
            direction = "RL"
        if direction == "BT":
            j = start_y
            for i in range(start_x - 1, -1, -1):
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = count
                count += 1
                start_x = i
            direction = "LR"
    return matrix


matrix = fill_spiral(4)
print_matrix(matrix)
