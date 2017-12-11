"""
Let's have some fun with 2D Matrices! 
Write a method find_spiral to traverse a 2D matrix (List of Lists) 
of ints in a clockwise spiral order and append the elements to an output List of Integers.

Example:
Input Matrix :      
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]

Output List:[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""


def find_spiral(matrix):
    rows = len(matrix) 
    cols = len(matrix[0]) 

    t_row = 0
    b_row = len(matrix) - 1
    
    f_col = 0
    l_col = len(matrix[0]) -1 
    
    
    