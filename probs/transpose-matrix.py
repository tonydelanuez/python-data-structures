def transpose_matrix(matrix):
    if len(matrix) <= 1:
        return matrix
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(i+1, cols):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    return matrix