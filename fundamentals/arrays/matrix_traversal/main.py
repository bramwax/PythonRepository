import solutions.row_wise as rowwise
import solutions.col_wise as colwise
import solutions.diagonal as diag

def main():

	print("running...")
	
	matrix = [['🦨','🐈','🐖','🐘'],
		   	  ['🐎','🐒','🐓','🐕'],
			  ['🐄','🐋','🐌','🐏'],
			  ['🐢','🐍','🐟','🐇']]
	
	print("Row-wise TLBR:", *rowwise.row_wise_tl_br(matrix))
	print("Row-wise TRBL:", *rowwise.row_wise_tr_bl(matrix))
	print("Row-wise BRTL:", *rowwise.row_wise_br_tl(matrix))
	print("Row-wise BLTR:", *rowwise.row_wise_bl_tr(matrix))
	print("-" * 63)
	print("Diagonal TLBR", *diag.diag_tl_br(matrix))
	print("Diagonal TRBL", *diag.diag_tr_bl(matrix))
	print("Diagonal BRTL", *diag.diag_br_tl(matrix))	
	print("Diagonal BLTR", *diag.diag_bl_tr(matrix))

if __name__ == "__main__":
	main()