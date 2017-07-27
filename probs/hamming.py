import sys

n = int(sys.argv[1])
count = 0
while(n > 0): 
	if((1 & n) is 1):
		print("it is 1")
		count += 1
	n = n >> 1
print(count)