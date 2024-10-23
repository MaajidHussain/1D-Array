NOTE:-
# Attempting to remove a non-existent element in the Array will lead to,
# Array.remove(100)  # This will raise a ValueError
# Use 3rd approach for this..
--------------------------------------------------------------------------------------

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


#-----------------------------------------------------------------------------------

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


#----------------------------------------------------------------------------------------
""" 3. Convert to List,
       Remove Elements
       Convert back to Array """
from array import array

# Initializing the array
third_array = array('i', [22, 55, 66, 77, 88, 99, 100, 121, 135])
print(f"Before deleting elements, size of the array is: {len(third_array)}\n")

# Deleting elements
# First, we can convert the array to a list for easier manipulation
temp_list = third_array.tolist()

# Remove the elements you want to delete
for element in [121, 88]:
    if element in temp_list:
        temp_list.remove(element)

# Convert the list back to an array
third_array = array('i', temp_list)

print(third_array)
print(f"After deleting elements, size of the array is: {len(third_array)}")
