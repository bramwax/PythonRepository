# Iterates through each row of matrix from left to right.
def row_wise_fwd(matrix):
    if len(matrix) == 0:
        return None
    else:
        wid, hgt = len(matrix[0]), len(matrix)
        iteration = []
        for row in range(0, hgt):
            for col in range(0, wid):
                iteration.append(matrix[row][col])
        return iteration


# Iterates through each row from right to left.
def row_wise_rev(matrix):
    if len(matrix) == 0:
        return None
    else:
        wid, hgt = len(matrix[0]), len(matrix)
        iteration = []
        for row in range(0, hgt):
            for col in range(wid - 1, -1, -1):
                iteration.append(matrix[row][col])
        return iteration
