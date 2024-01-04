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
