with open("day2.txt", "r") as file:
    lines = file.readlines()

matrix = [list(map(int, line.split())) for line in lines]
rows = len(matrix)
cols = len(matrix[0])
safe = 0
for row in matrix:
    l,r = 0,1
    increasing = True
    if row[l] > row[r]: increasing = False
    while r < len(row):
        if increasing and row[l] <= row[l] and (row[r] - row[l] > 3 or row[r] - row[l] < 1): 
            break
        if not increasing and row[l] >= row[l] and (row[l] - row[r] > 3 or row[l] - row[r] < 1): 
            break
        r += 1
        l += 1
    if l == len(row) - 1: safe += 1
print(safe)

