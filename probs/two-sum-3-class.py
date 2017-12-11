"""
Design and implement a TwoSum class. It should support the following operations: add and find. 
add(input) – Add the number input to an internal data structure. 
find(value) – Find if there exists any pair of numbers which sum is equal to the value. 

For example, 
add(1); 
add(3); 
add(5); 
find(4) -> true; find(7) -> false 
Example:
"""

class TwoSum(object):
    def __init__(self):
        self.arr = {}

    def add(self, num):
        if num in self.arr:
            self.arr[num] += 1
        else:
            self.arr[num] = 1
        print(self.arr)

    def find(self, num):
        target = num
        for val in self.arr:
            compl = target - val 
            if compl in self.arr:
                if compl == val:
                    if self.arr[compl] > 1:
                        return True
                else: 
                    if self.arr[compl] > 0: 
                        return True
        print("False")
        return False

test = TwoSum()
test.add(1)
test.add(3)
test.add(5)
print(test.find(4))
print(test.find(7))


