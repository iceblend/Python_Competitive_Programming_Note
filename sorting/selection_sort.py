arr = [8, 5, 4, 7, 2]

''' Selection Sort '''
for i in range(len(data)):
    min_index = i # The index of the minimum value.
    for j in range(i + 1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i] # Swap.

for x in data:
    print(x)