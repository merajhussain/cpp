
def targetsum(arr,target):

    arr.sort()
    l=0
    r=len(arr)-1
    while l<r:
        if arr[l]+arr[r]==target:
            return True
        else:
            if arr[l]+arr[r]>target:
                r-=1
            else:
                l+=1
    return False


print(targetsum([2,7,11,15], 9))
print(targetsum([3,2,4], 6))
print(targetsum([3,3], 6))
print(targetsum([1,2,3,4,5], 5))
print(targetsum([1,1,1,2,2], 3))
print(targetsum([0,0], 0))
print(targetsum([0,1,2,3], 3))
print(targetsum([-1,-2,-3,-4,-5], -8))
print(targetsum([-1,0,1,2,-1,-4], 0))
print(targetsum([10,20,30], 100))
print(targetsum([1], 2))
print(targetsum([], 0))


