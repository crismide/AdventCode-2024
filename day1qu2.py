import collections


with open('day1in1.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        values = line.split()  
        column1.append(int(values[0])) 
        column2.append(int(values[1]))

hash_repeated = collections.defaultdict(list)

for num in column1:
    if num in hash_repeated.keys(): 
        hash_repeated[num][1] += 1
    else:
        hash_repeated[num] = [0,1]



for num in column2:
    if num in hash_repeated.keys(): hash_repeated[num][0] += num
res = 0

for key,value in hash_repeated.items():
    res += value[0] * value[1]
print(res)