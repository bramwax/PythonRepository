# 1) Iterate through each row, then move to the next row.
def row_wise(matrix):
    
    output = ""
    for row in range(0, len(matrix[0])):
        for col in range(len(matrix)):
            output += f"{matrix[row][col]},"
            
    print(output[:-1])

# 2) Traverse each row in reverse order.
def reverse_row_wise(matrix):
    return None

# --------------------------------------------------------------------------------------------------------

# 3) Iterate through each column, then move to the next column.
def col_wise(matrix):
    return None

# 4) Traverse each column in reverse order.
def reverse_col_wise(matrix):
    return None

# --------------------------------------------------------------------------------------------------------

# 5) Traverse the outer edges of a two-dimensional array in a clockwise direction.
def boundary(matrix):
    return None

# 6) Traverse outer edges of a two-dimensional array in an anti-clockwise direction.
def reverse_boundary(matrix):
    return None

# --------------------------------------------------------------------------------------------------------

# 7) Traverse the elements diagonally, from the top-left corner to the bottom-right corner.
def primary_diagonal(matrix):
    return None

# 8) Traverse the elements diagonally, from the bottom-right corner to the top-left corner.
def reverse_primary_diagonal(matrix):
    return None

# --------------------------------------------------------------------------------------------------------

# 9) Traverse the elements diagonally, from one corner from the top-right corner to the bottom-left corner.
def secondary_diagonal(matrix):
    return None


# 10) Traverse the elements diagonally, from one corner from the bottom-left to the top-right corner.
def reverse_secondary_diagonal(matrix):
    return None

# --------------------------------------------------------------------------------------------------------

# 11) Move in a spiral pattern from the outermost layer towards the center, from the top-left corner.
def spiral(matrix):
    return None


# Move in a spiral pattern from the center to the top-left corner of the outermost layer.
def reverse_spiral(matrix):
    return None










# print values in each row on a single line
'''
for row in grid:
    tmp_row = ""
    for col in row:
        tmp_row = tmp_row + str(col)
        if col < 10:
            tmp_row = tmp_row + "  "
        else:
            tmp_row = tmp_row + " "

    print (tmp_row)
'''

# print values in each column on a single line
'''
for a in range(4):
    tmp_col = ""
    for b in range(4):
        tmp_col = tmp_col + str(grid[b][a])
        if grid[b][a] < 10:
            tmp_col = tmp_col + "  "
        else:
            tmp_col = tmp_col + " "
    print(tmp_col)
'''

# print values on each of the two diagonals on single lines
'''
top_bottom = ""
bottom_top = ""
for i in range(4):
    top_bottom += str(grid[i][i]) + " "
    bottom_top += str(grid[(len(grid[0])-1)-i][i]) + " "
    
print(top_bottom)
print(bottom_top)
'''

# print values in a clockwise spiral from top left
'''
width, height = len(grid[0]), len(grid)
total_items = width * height

print(f"{width} x {height} = {total_items} items to print.")

row, col = 0, 0
moving = "right"
output = ""
sub = 0



while True:

    if moving == "right":
        output += str(grid[row][col]) + ","
        if col < (width -1) - sub:
            col += 1
        else:
            moving = "down"
            row += 1
            
    elif moving == "down":
        output += str(grid[row][col]) + ","
        row += 1
        if row < (height -1) - sub:
            row += 1
        else:
            moving = "left"
            col -= 1
            break

print(output[:-1])
'''



# A 2D array is assigned to the variable with the idenifier grid
matrix = [[5 ,13,7 ,9 ],
          [21,11,13,7 ],
          [16,33,79,3 ],
          [6 ,15,71,52]]

row_wise(matrix)



