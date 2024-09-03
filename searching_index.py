from array import *
def LinearSearch(arr,target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return "Target Not Found"
array=array('i',[21,45,65,8,78,45,65,21,54,45,4,12])
print(LinearSearch(array,78))
print(LinearSearch(array,65))
print(LinearSearch(array,45))
print(LinearSearch(array,21))