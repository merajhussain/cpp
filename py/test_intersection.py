from intersection import intersect


def test_intersection1():
    arr1=[2,3,3,5,7,11]
    arr2=[3,3,7,15,31]
    inter= [3,3,7]
    assert inter == intersect(arr1,arr2)

def test_intersection2():
    arr1=[1,2,4]
    arr2=[3,5,6]
    inter = []
    assert inter == intersect(arr1,arr2)

def test_intersection3():
    arr1=[]
    arr2=[1,2,3]
    inter = []
    assert inter == intersect(arr1,arr2)

def test_intersection4():
    arr1=[1,1,1,2,2]
    arr2=[1,1,1,1,2]
    inter = [1,1,1,2]
    assert inter == intersect(arr1,arr2)

def test_intersection5():
    arr1=[7, 3, 2, 3, 11, 5]
    arr2= [31, 3, 7, 3, 15]
    inter = [3,3,7]
    assert inter == intersect(arr1,arr2)
