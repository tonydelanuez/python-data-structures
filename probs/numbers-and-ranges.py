"""

Given a sorted list and an input number as inputs, write a function to return a Range object, consisting of the indices of the first and last occurrences of the input number in the list. Check out the Use Me section to examine the structure of the Range class.

Note: The List can have duplicate numbers. The indices within the Range object should be zero based.

"""
def find_range(input_list,input_number):
    # Example list: [1,2,5,5,8,8,10]
    # Input Number: 8
    # Output: [4,5]
    
    first = 0 
    last = 0
    started = False
    for index, val in enumerate(input_list):
        if val == input_number and not started:
            first = last = index
            started = True
        elif val == input_number and started:
            last = index
    return Range(first,last)