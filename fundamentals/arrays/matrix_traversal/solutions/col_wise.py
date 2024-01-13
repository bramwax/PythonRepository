# Traverse matrix from top-left to bottom-right corner
def col_wise_tl_br(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:
		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loops
		# for n in range(0, n_cols):
		# 	for m in range(0, m_rows):
		# 		result.append(matrix[m][n])

		# using while loops
		n = 0
		while n < n_cols:
			m = 0
			while m < m_rows:
				result.append(matrix[m][n])
				m += 1
			n += 1

		return result

# Traverse matrix from top-right to bottom-left corner
def col_wise_tr_bl(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:
		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loops
		# for n in range(n_cols-1, -1, -1):
		# 	for m in range(0, m_rows):
		# 		result.append(matrix[m][n])

		# using while loops
		m = 0
		while m < m_rows:
			n = n_cols - 1
			while n > -1:
				result.append(matrix[m][n])
				n -= 1
			m += 1

	return result

# Traverse matrix from bottom-right to top-left corner
def col_wise_br_tl(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:
		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loops
		# for m in range(m_rows-1, -1, -1):
		# 	for n in range(n_cols-1, -1,-1):
		# 		result.append(matrix[m][n])

		# while loops
		m = m_rows-1
		while m > -1:
			n = n_cols-1
			while n > -1:
				result.append(matrix[m][n])
				n -= 1
			m -= 1

	return result

# Traverse matrix from bottom-left to top-right corner
def col_wise_bl_tr(matrix):

	if len(matrix) == 0 or len(matrix[0]) == 0:
		return None
	else:
		result = []
		m_rows = len(matrix)
		n_cols = len(matrix[0])

		# using for loops
		# for m in range(m_rows-1, -1, -1):
		# 	for n in range(0, n_cols):
		# 		result.append(matrix[m][n])

		# using while loops
		m = m_rows-1
		while m > -1:
			n = 0
			while n < n_cols:
				result.append(matrix[m][n])
				n += 1
			m -= 1

		return result