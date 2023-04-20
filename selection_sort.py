def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
    
    return data
data = [1,4,8,2,4,9,3,9,5]
sorted_data = selection_sort(data)
print(sorted_data)