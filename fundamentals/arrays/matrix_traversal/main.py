import solutions.row_wise as rw
import solutions.col_wise as cw

def main():
    matrix = [['🍌','🍎','😃','🐉'],
              ['👺','🍺','🍩','🚴'],
              ['🚘','🦑','🚆','🏝'],
              ['🌆','🛹','🕺','🍕']]
    
    print(rw.row_wise_fwd(matrix))
    print(rw.row_wise_rev(matrix))
    print(cw.col_wise_fwd(matrix))
    print(cw.col_wise_rev(matrix))

if __name__ == "__main__":
    main()
