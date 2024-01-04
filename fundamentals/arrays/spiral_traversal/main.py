def add_to_result(num_in):
    global result
    result = result + str(num_in) + ", "
    global count
    count += 1

# A 2D array is assigned to the variable with the idenifier grid
grid = [[5 ,13,7 ,9 ],
        [21,11,13,7 ],
        [16,33,79,3 ],
        [6 ,15,71,52]]

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

row = 0
col = 0
status = "right"
count = 0
result = ""
sub = 0

total = len(grid[0]) * len(grid[0])

while True:

    if status == "right":
        num = grid[row][col]
        print(num)
        add_to_result(num)
        row += 1
        if row > len(grid[col]) - sub:
            status = "down"
            row -= 1
            col += 1

    elif status == "down":
        num = grid[col][len(grid[col]) - sub]
        add_to_result(num)
        col += 1
        if col > len(grid):
            status = "left"
            col -= 1
            row = len(grid[col]-1)

    elif status == "left":
        num = grid[col][row]
        add_to_result(num)
        row -= 1
        if row < 0 + sub:
            status = "up"
            row = 0
            col -= 1
            sub += 1

    else:
        num = grid[col][row]
        add_to_result(num)
        col -= 1
        if col < 0 + sub:
            status = "right"
            row += 1
            col += 1

    if count >= total:
        break
