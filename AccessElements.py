from array import *
def accessElements(Array,index):
    if index >=len(Array):
        print(f"There is no element at index:- {index}.")
    else:
        print(f"Element at index:{index} is",Array[index])
Array=array('i',[21,35,64,48,98,54,12,34,65,54,78,79,16,10])

accessElements(Array,len(Array)+1)
accessElements(Array,12)