def tick(matrix: list[list[bool]]) -> list[list[bool]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    new_matrix = [[False] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            live_neighbors = sum(
                matrix[x][y]
                for x in range(max(0, i-1), min(rows, i+2))
                for y in range(max(0, j-1), min(cols, j+2))
                if (x, y) != (i, j)
            )
            if matrix[i][j]:
                new_matrix[i][j] = live_neighbors in [2, 3]
            else:
                new_matrix[i][j] = live_neighbors == 3
    
    return new_matrix
