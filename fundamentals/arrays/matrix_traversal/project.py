'''
[['🍌','🍎','😃','🐉'],
 ['👺','🍺','🍩','🚴'],
 ['🚘','🦑','🚆','🏝'],
 ['🌆','🛹','🕺','🍕']]
     
1. Row-wise Traversal:

    Forward: Iterate through each row from left to right.
    >>>['🍌','🍎','😃','🐉','👺','🍺','🍩','🚴','🚘','🦑','🚆','🏝','🌆','🛹','🕺','🍕']
    
    Reverse: Iterate through each row from right to left.
    >>>['🐉','😃','🍎','🍌','🚴','🍩','🍺','👺','🏝','🚆','🦑','🚘','🍕','🕺','🛹','🌆']

2. Column-wise Traversal:

    Forward: Iterate through each column from top-left to bottom-right.
    >>>['🍌','👺','🚘','🌆','🍎','🍺','🦑','🛹','😃','🍩','🚆','🕺','🐉','🚴','🏝','🍕']
    
    Reverse: Iterate through each column from bottom-left to top-right.
    >>>['🌆','🚘','👺','🍌','🛹','🦑','🍺','🍎','🕺','🚆','🍩','😃','🍕','🏝','🚴','🐉']
    

3. Diagonal Traversal:

    Primary:
        Forward: Top-left to bottom-right.
        >>>['🍌','🍺','🚆','🍕']
        
        Reverse: Bottom-right to top-left.
        >>>['🍕','🚆','🍺','🍌']
        
    Secondary:
        Forward: Top-right to bottom-left.
        >>>['🐉','🍩','🦑','🌆']
        
        Reverse: Bottom-left to top-right.
        >>>['🌆','🦑','🍩','🐉']

        
4. Boundary Traversal:

    [['🍌','🍎','😃','🐉'],
     ['👺','🍺','🍩','🚴'],
     ['🚘','🦑','🚆','🏝'],
     ['🌆','🛹','🕺','🍕']]
     
    Top:
        Forward: Left to right.
        >>>['🍌','🍎','😃','🐉']
        Reverse: Right to left.
        >>>['🐉','😃','🍎','🍌']
        
    Right:
        Forward: Top to bottom.
        >>>[,,,]
        
        Reverse: Bottom to top.
        >>>[,,,]
        
    Bottom:
        Forward: Left to right.
        >>>['🌆','🛹','🕺','🍕']
        
        Reverse: Right to left.
        >>>[,,,]
        
    Left:
        Forward: Top to bottom.
        >>>[,,,]
        
        Reverse: Bottom to top.
        >>>[,,,]
        
    Full:
        Forward: From top-left corner.
        >>>[]
        
        Reverse: From top-left corner.
        >>>[]
        
7. Zigzag Traversal:

    row_first: Traverse rows left to right, then right to left, and repeat.
    >>>['🍌','👺','🍎','😃','🍺','🚘','🌆','🦑','🍩','🐉','🚴','🚆','🛹','🕺','🏝','🍕']
        
    col_first: Traverse rows right to left, then left to right, and repeat.
    >>>['🍌','🍎','👺','🚘','🍺','😃','🐉','🍩','🦑','🌆','🛹','🚆','🚴','🏝','🕺','🍕']

8. Snake Traversal:
    Forward: Traverse rows left to right, then right to left, and move to the next row.
    Reverse: Traverse rows right to left, then left to right, and move to the next row.
    Down: Traverse columns top to bottom, then right to left, and move to the next row.
    Up: Traverse columns bottom to top, then top to bottom, and move to the next column.

9. Column-wise Zigzag Traversal:
    Forward: Traverse columns top to bottom, then bottom to top, and repeat.
    Reverse: Traverse columns bottom to top, then top to bottom, and repeat.

10. Diagonal Zigzag Traversal:
    Forward: Traverse diagonals left to right, then right to left, and repeat.
    Reverse: Traverse diagonals right to left, then left to right, and repeat.

11. Clockwise Diagonal Spiral:
    Forward: Move in a clockwise spiral pattern along both diagonals.
    Reverse: Move in a counter-clockwise spiral pattern along both diagonals.

12. Anti-clockwise Diagonal Spiral:
    Forward: Move in an anti-clockwise spiral pattern along both diagonals.
    Reverse: Move in a clockwise spiral pattern along both diagonals.
'''

matrix = [['🍌','🍎','😃','🐉'],
          ['👺','🍺','🍩','🚴'],
          ['🚘','🦑','🚆','🏝'],
          ['🌆','🛹','🕺','🍕']]
