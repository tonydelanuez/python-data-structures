"""

Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.

Limits

1 ≤ T ≤ 100.
Small dataset

0 ≤ N ≤ 200.
Large dataset

0 ≤ N ≤ 106.

Sample
Input 
5
0
1
2
11
1692

Output
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076


"""
def counting_sheep(n):
	# Store all the digits in a list to check and make sure we have them all. 
	digits = [0,1,2,3,4,5,6,7,8,9]
	# Run this for each test
	val_map = {}
	for value in n:
		# Break condition for value 0
		if value == 0:
			val_map[value] = "INSOMNIA"
		else:
			seen = set()
			inc = 1
			while list(seen) != digits:
				result = value * inc
				# Basically appending the values for each digit into the "seen digits"
				seen = seen.union([int(d) for d in str(result)])
				#print(seen)
				inc += 1
			print(result)
			val_map[value] = result


def run():
	tests = [0, 1, 2, 11, 1692]
	counting_sheep(tests)

run()

















