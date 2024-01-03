# Each pixel of a 6x6 gif image is stored in a 2D array.
# Each pixel is represented by 2-digit hex code.

# print(bin(112))
# gif_image = [[0x22,0x22,0x22,0x22,0x22,0x22],
#              [0x6A,0x6A,0x6A,0x6A,0x6A,0x6A],             
#              [0x6E,0x6E,0x6E,0x6E,0x6E,0x6E],
#              [0x40,0x40,0x40,0x40,0x40,0x40],
#              [0x19,0x19,0x19,0x19,0x19,0x19],
#              [0x31,0x31,0x31,0x31,0x31,0x31]]
# print(int(gif_image[0][0]))

image = [["A","A","A","A"],
         ["B","B","B","B"],
         ["C","C","C","C"],
         ["D","D","D","D"]]

new_image = []
for row in range(0,4):
    tmp_array = []
    for col in range(0,4):
        tmp_array.append(None)
    
    new_image.append(tmp_array)

print(*new_image, sep="\n")

for row in range(0,4):
    for col in range(0,4):
        new_image[col][3-row] = image[row][col]

print(*new_image, sep="\n")
