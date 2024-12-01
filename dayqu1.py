with open('day1in1.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        values = line.split()  
        column1.append(int(values[0])) 
        column2.append(int(values[1]))

sorted_c1 = sorted(column1)
sorted_c2 = sorted(column2)
res = 0

for i in range(len(column1)):
    res += abs(sorted_c1[i] - sorted_c2[i])
print(res)