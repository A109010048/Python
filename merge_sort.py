def merge(left, right):
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result = result + left if len(left) else result + right
    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    return merge(merge_sort(left_array), merge_sort(right_array))

arr = [1,4,7,2,8,2,0]
array_sort = merge_sort(arr)
print(array_sort)