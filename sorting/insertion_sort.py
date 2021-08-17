arr = [8, 5, 4, 7, 2]

''' Insertion Sort '''
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
        else:
            break

print(arr)