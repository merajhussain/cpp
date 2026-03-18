def array_advance(elems):
    farthest_reached=0
    i=0
    while i<len(elems):
        if i > farthest_reached:
            return False
        farthest_reached=max(farthest_reached,i+elems[i])
        i+=1
    return True



