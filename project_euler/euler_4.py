numA = 100
pal = 0

while numA <= 999:
  numB = numA
  while numB <= 999:
    prd = str(numA * numB)
    slice_size = len(prd) // 2
    lft_slice = prd[:slice_size]
    rgt_slice = prd[slice_size * -1:][::-1]

    if lft_slice == rgt_slice:
      if int(prd) > pal:
        pal = int(prd)

    numB += 1
  numA += 1

print(pal)