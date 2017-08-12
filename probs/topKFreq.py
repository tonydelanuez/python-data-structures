# return the top frequency of a number
nums = [1,1,1,2,2,3,7,8,5,5,3,3,3,4,2,9,9,9,6]
k = 2
#return[1,2]

freq = {}
for val in nums:
	# 
	if(val not in freq):
		freq[val] = 1
	else:
		freq[val] += 1


ksize = []
for i in range(k):
	ksize.append((i+1,0));

print(freq)
print(ksize)