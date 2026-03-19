
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




