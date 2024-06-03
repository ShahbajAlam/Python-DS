def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_item = arr[i]
        j = i - 1
        while current_item < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            arr[j] = current_item
            j -= 1
    return arr


print(insertion_sort([7, 1, 3, 6, 4, 5, 2]))
