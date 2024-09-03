from array import *
'''
1.Deleting an element using element's value.
'''
first_array=array('i',[21,45,78,98,65,45,21,32])
print(f"Before removing Elements, size of the array is:",len(first_array),"\n")
first_array.remove(45)
first_array.remove(65)
print(first_array)
print(f"After removing Elements, size of the array is:",len(first_array))


#---------------------------------------------------------------------------

from array import *
'''
2.Deleting an element using index's number.
'''
second_array=array('i',[22,55,66,77,88,99,100,121,135])
print(f"Before deleting Elements, size of the array is:",len(second_array),"\n")
second_array.pop()
second_array.pop(0)
second_array.pop(len(second_array)-1)
second_array.pop(5)
print(second_array)
print(f"After deleting Elements, size of the array is:",len(second_array))


#-----------------------------------------------------------------------------------

from array import *
'''
3.Deleting an element using delete().
'''
third_array=array('i',[22,55,66,77,88,99,100,121,135])
print(f"Before deleting Elements, size of the array is:",len(third_array),"\n")
third_array.remove(121)
third_array.remove(88)
print(third_array)
print(f"After deleting Elements, size of the array is:",len(third_array))
