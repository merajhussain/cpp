import math

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


def biotonic_peak(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        ml = arr[mid-1] if mid - 1 >=0 else float("-inf")
        me = arr[mid]
        mr = arr[mid+1] if mid + 1 < len(arr) else float("inf")
        if ml < me and mr > me:
            low = mid + 1
        elif ml > me and mr < me:
            high = mid - 1
        elif ml<me and mr < me:
            return me
    return None

def integer_sqrt(k):
    low = 0
    high = k - 1
    while low <= high:
        mid = (low + high) // 2
        if mid *mid <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low-1

def integer_sqr_root(k):
    return int(math.sqrt(k))

def closest_number(arr, num):
    low = 0
    high = len(arr) - 1
    closest = arr[0]

    while low <= high:
        mid = (low + high) // 2

        if abs(arr[mid] - num) < abs(closest - num):
            closest = arr[mid]

        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return arr[mid]

    return closest

