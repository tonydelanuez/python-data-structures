def transpose_matrix(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	temp = 0

	for j in range(cols): 
		for i in range(i + 1,rows):
			temp = matrix[j][i]
			matrix[j][i] = matrix[i][j]
			matrix[i][j] temp 