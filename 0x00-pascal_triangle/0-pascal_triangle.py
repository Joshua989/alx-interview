def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = [1]  # First element of every row is always 1
        
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            
            row.append(1)  # Last element of every row is always 1
        
        triangle.append(row)
    
    return triangle

