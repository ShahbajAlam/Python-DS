def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_arr = [x for x in arr[1:] if x <= pivot]
    right_arr = [x for x in arr[1:] if x > pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
