def string_compression(s):
	# Keep track of the current character in order to make a comparison with the "next" or "previous" element. 
	current_char = s[0]
	result = ""
	counter = 1
	# Loop through the rest of the list. If the same character found, increment counter. Otherwise, append the letter and count to the result.
	for i in s[1::]:
		if i == current_char:
			counter += 1
		else:
			result += str(current_char) + str(counter)
			counter = 1
		current_char = i
	result += str(current_char) + str(counter)
	return result

print(string_compression("aaaabcccccaaa"))


