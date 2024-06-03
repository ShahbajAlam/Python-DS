def binary_search(arr: list, target: int) -> int:
    first_index = 0
    last_index = len(arr) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2

        if target == arr[mid_index]:
            return mid_index
        elif target < arr[mid_index]:
            last_index = mid_index - 1
        else:
            first_index = mid_index + 1

    return -1


print(binary_search([10, 20, 30, 40, 50, 60], 20))
