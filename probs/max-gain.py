import sys
def max_gain(input_list):
    # find smallest element
    # keep taking difference at every step
    # return max difference
    if len(input_list) == 0:
        return None
    if len(input_list) == 1:
        return input_list[0]
        
    min_val = input_list[0]
    max_diff = 0
    for val in input_list[1:]:
        max_diff = max(max_diff, val - min_val)
        min_val = min(min_val, val)
    return max_diff