# Import 50 names from file, place in array names, and print
all_names = []
file = open('names.txt')
for item in file:
    all_names.append(item.rstrip())
file.close()

for index in range(len(all_names)):
    print(f'{str(index+1).zfill(2)} | {all_names[index]}')