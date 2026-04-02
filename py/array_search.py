def linear_search(arr,value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


def binary_search(arr,value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low= mid + 1
    return -1


def fixed_number(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == arr[mid]:
            return mid
        if arr[mid] < mid:
            low = mid + 1
        elif arr[mid] > mid:
            high = mid - 1
    return None

