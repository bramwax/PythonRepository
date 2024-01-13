# Traverse matrix diagonally from top-left to bottom-right corner
def diag_tl_br(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:

		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])
		diagonal = min(m_rows, n_cols)

		# using for loop
		# for index in range(diagonal):
		# 	result.append(matrix[index][index])

		# using while loop
		index = 0
		while index < diagonal:
			result.append(matrix[index][index])
			index += 1

		
	return result

# Traverse matrix diagonally from top-right to bottom-left corner
def diag_tr_bl(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:

		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loop

		# using while loop

		
	return result

# Traverse matrix diagonally from bottom-right to top-left corner
def diag_br_tl(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:

		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loop

		# using while loop

		
	return result

# Traverse matrix diagonally from bottom-left to top-right corner
def diag_bl_tr(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:

		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loop

		# using while loop

		
	return result