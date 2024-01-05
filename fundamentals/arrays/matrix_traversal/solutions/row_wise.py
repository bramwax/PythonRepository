# Row-wise Traversal:
# ------------------------------------------------------------------------------------------
# Iterates through each row of matrix from left to right.
# ['🍌','🍎','😃','🐉','👺','🍺','🍩','🚴','🚘','🦑','🚆','🏝','🌆','🛹','🕺','🍕']

def row_wise_fwd(matrix):
    if len(matrix) == 0:
        return None
    else:
        wid, hgt = len(matrix[0]), len(matrix)
        iteration = []
        for x in range(0, hgt):
            for y in range(0, wid):
                iteration.append(matrix[x][y])
        return iteration


# Reverse: Iterate through each row from right to left.
# ['🐉','😃','🍎','🍌','🚴','🍩','🍺','👺','🏝','🚆','🦑','🚘','🍕','🕺','🛹','🌆']

def row_wise_rev(matrix):
    return "row_wise_rev executed"

matrix = [['🍌','🍎','😃','🐉'],
          ['👺','🍺','🍩','🚴'],
          ['🚘','🦑','🚆','🏝'],
          ['🌆','🛹','🕺','🍕']]
