def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if target<arr[mid]:
            high=mid-1
        if target>arr[mid]:
            low=mid+1
    return -1
a = [10, 20, 30, 40, 50, 60, 70, 80]
binary_search(a, 80)
