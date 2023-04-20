def quick_sort(array):
    n = len(array)
    if n < 2:
        return array
    left = []
    right = []
    pivot = array[0]
    for i in range(1,n):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [3,0,6,1,39,2]
sort_arr = quick_sort(arr)
print(sort_arr)