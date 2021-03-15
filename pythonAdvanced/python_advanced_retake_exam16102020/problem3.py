def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for row_index in range(2, n):
        new_row = []
        for cell_index in range(row_index + 1):
            cell_value = 0
            if 0 <= cell_index - 1 < len(triangle[row_index - 1]):
                cell_value += triangle[row_index - 1][cell_index - 1]

            if 0 <= cell_index < len(triangle[row_index - 1]):
                cell_value += triangle[row_index - 1][cell_index]

            new_row.append(cell_value)
        triangle.append(new_row)

    return triangle

print(get_magic_triangle(5))

