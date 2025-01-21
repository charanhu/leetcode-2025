def merge_sort(arr):
    """
    Sorts the list 'arr' in ascending order using the merge sort algorithm.
    """
    # If the array has 0 or 1 elements, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Find the middle index to split the array
    mid = len(arr) // 2
    
    # Recursively sort the left half
    left_half = merge_sort(arr[:mid])
    
    # Recursively sort the right half
    right_half = merge_sort(arr[mid:])
    
    # Merge the two sorted halves into one sorted list
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists 'left' and 'right' into a single sorted list.
    """
    merged = []    # This will store the merged result
    i, j = 0, 0    # Pointers to current index in left and right
    
    # Compare elements from 'left' and 'right' and pick smaller one each time
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # If any elements remain in left or right, add them
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Example usage:
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", data)
    sorted_data = merge_sort(data)
    print("Sorted:  ", sorted_data)
