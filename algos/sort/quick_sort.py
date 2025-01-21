def quick_sort(arr):
    # Base case: A list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # 1. Pick the first element as pivot
    pivot = arr[0]

    # 2. Divide the rest into 'left' and 'right'
    left = [x for x in arr[1:] if x <= pivot]
    print("left: ", left)
    right = [x for x in arr[1:] if x > pivot]
    print("right: ", right)

    # 3. Recursively quick-sort the left and right parts
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # 4. Combine left, pivot, and right
    return sorted_left + [pivot] + sorted_right

# Example usage:
numbers = [7, 2, 1, 6, 8, 5, 3, 4]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8]
