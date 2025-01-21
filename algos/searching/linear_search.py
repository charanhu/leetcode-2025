def linear_search(arr, target):
    """
    Returns the index of 'target' in 'arr' using linear search,
    or -1 if not found.
    """
    for i in range(len(arr)):
        # Check if element at index i matches target
        if arr[i] == target:
            return i
    return -1


# Example usage:
if __name__ == "__main__":
    data = [10, 15, 3, 7]
    print("Data:", data)
    idx = linear_search(data, 7)
    print("Element 7 found at index:", idx)
