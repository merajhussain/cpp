def intersect(arr1, arr2):
    inter=[]
    i = 0
    j = 0
    arr1.sort()
    arr2.sort()
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            inter.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i +=1
        else:
            j +=1
    return inter




