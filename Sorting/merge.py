def merge(list1, list2):
    i = j = 0
    combined = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_index = len(arr) // 2
    left_arr = merge_sort(arr[:mid_index])
    right_arr = merge_sort(arr[mid_index:])

    return merge(left_arr, right_arr)
