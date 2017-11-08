def merge_ranges(input_range_list):
	#check for null or 1 list
	if (len(input_range_list) <= 1 or input_range_list == None):
		return input_range_list
	output = []
	i = 1
	previous = input_range_list[0]
	while i < len(input_range_list):
		current = input_range_list[i]
		#overlap exists
		if(previous.upper_bound >= current.lower_bound):
			#make a new merged range
			merged = Range(previous.lower_bound, max(previous.upper_bound, current.upper_bound))
			previous = merged
		else:
			#only append when we can no longer merge
			output.append(previous)
			previous = current
		i += 1
	output.append(previous)
	return output

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1
    
    def __init__(self,lower_bound,upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
 
    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"
