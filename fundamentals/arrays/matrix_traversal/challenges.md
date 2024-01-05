# Matrix (2D Array) Traversal

[['🍌','🍎','😃','🐉'],  
&nbsp;['👺','🍺','🍩','🚴'],  
&nbsp;['🚘','🦑','🚆','🏝'],  
&nbsp;['🌆','🛹','🕺','🍕']]

## Challenges  
*For each of the following create a function that takes a dynamic 2D array (various sizes of matrix), and returns a 1D array containing the output (items) from the given traversal. The best approach would be to create separate files for each of the numbered challenges and import these into a central main.py file for testing.*

1. Row-wise Traversal:
    >Forward: Iterate through each row from left to right.  
    >['🍌','🍎','😃','🐉','👺','🍺','🍩','🚴','🚘','🦑','🚆','🏝','🌆','🛹','🕺','🍕']
    
    >Reverse: Iterate through each row from right to left.  
    >['🐉','😃','🍎','🍌','🚴','🍩','🍺','👺','🏝','🚆','🦑','🚘','🍕','🕺','🛹','🌆']

2. Column-wise Traversal:

    >Forward: Iterate through each column from top-left to bottom-right.  
    >['🍌','👺','🚘','🌆','🍎','🍺','🦑','🛹','😃','🍩','🚆','🕺','🐉','🚴','🏝','🍕']
    
    >Reverse: Iterate through each column from bottom-left to top-right.  
    >['🌆','🚘','👺','🍌','🛹','🦑','🍺','🍎','🕺','🚆','🍩','😃','🍕','🏝','🚴','🐉']

3. Diagonal Traversal:  

    * Primary:  
        >Forward: Top-left to bottom-right.  
        >['🍌','🍺','🚆','🍕']

        >Reverse: Bottom-right to top-left.  
        >['🍕','🚆','🍺','🍌']

    * Secondary:
        >Forward: Top-right to bottom-left.  
        >['🐉','🍩','🦑','🌆']

        >Reverse: Bottom-left to top-right.  
        >['🌆','🦑','🍩','🐉']

4. Boundary Traversal:
     
    * Top:  
        >Forward: Left to right.  
        >['🍌','🍎','😃','🐉']

        >Reverse: Right to left.  
        >['🐉','😃','🍎','🍌']
        
    * Right:  
        >Forward: Top to bottom.  
        >['🐉','🚴','🏝','🍕']

        > Reverse: Bottom to top.  
        >['🍕','🏝','🚴','🐉']
        
    * Bottom:  
        >Forward: Left to right.  
        >['🌆','🛹','🕺','🍕']
        
        >Reverse: Right to left.  
        >['🍕','🕺','🛹','🌆']
        
    * Left:  
        >Forward: Top to bottom.  
        >['🍌','👺','🚘','🌆']
        
        >Reverse: Bottom to top.  
        >['🌆','🚘','👺','🍌']
        
    * Full:
        >Forward: From top-left corner clockwise.  
        >['🍌','🍎','😃','🐉','🚴','🏝','🍕','🕺','🛹','🌆','🚘','👺']
        
        >Reverse: From top-left corner anticlockwise.  
        >['🍌','👺','🚘','🌆','🛹','🕺','🍕','🏝','🚴','🐉','😃','🍎']
        
5. Zigzag Traversal:

    >Row First: Traverse rows left to right, then right to left, and repeat.  
    >['🍌','👺','🍎','😃','🍺','🚘','🌆','🦑','🍩','🐉','🚴','🚆','🛹','🕺','🏝','🍕']
        
    >Column First: Traverse rows right to left, then left to right, and repeat.  
    >['🍌','🍎','👺','🚘','🍺','😃','🐉','🍩','🦑','🌆','🛹','🚆','🚴','🏝','🕺','🍕']

6. Snake Traversal:

    >Forward: Traverse rows left to right, then right to left, and move to the next row.  
    >['🍌','🍎','😃','🐉','🚴','🍩','🍺','👺','🚘','🦑','🚆','🏝','🍕','🕺','🛹','🌆']
    
    >Reverse: Traverse rows right to left, then left to right, and move to the next row.  
    >['🐉','😃','🍎','🍌','👺','🍺','🍩','🚴','🏝','🚆','🦑','🚘','🌆','🛹','🕺','🍕']
    
    >Down: Traverse columns top to bottom, then right to left, and move to the next row.  
    >['🍌','👺','🚘','🌆','🛹','🦑','🍺','🍎','😃','🍩','🚆','🕺','🍕','🏝','🚴','🐉']
    
    > Up: Traverse columns bottom to top, then top to bottom, and move to the next column.  
    >['🌆','🚘','👺','🍌','🍎','🍺','🦑','🛹','🕺','🚆','🍩','😃','🐉','🚴','🏝','🍕']

7. Spiral Traversal:

    >Forward: Move in a clockwise spiral pattern from the top-left.  
    >['🍌','🍎','😃','🐉','🚴','🏝','🍕','🕺','🛹','🌆','🚘','👺','🍺','🍩','🚆','🦑']
    
    >Reverse: Move in a counter-clockwise spiral pattern from the top-left.  
    >['🍌','👺','🚘','🌆','🛹','🕺','🍕','🏝','🚴','🐉','😃','🍎','🍺','🦑','🚆','🍩']
