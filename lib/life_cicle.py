def life_cicle(lines, columns, cells_matrix, board_cells):
    """Define a morte ou criação de celulas de acordo com as regras do jogo"""

    line = []
    for i in range(lines):
        column = []
        for j in range(columns):
            cells = 0
            if i > 0 and j > 0:
                if cells_matrix[i - 1][j - 1] == 1:
                    cells += 1
            if i > 0:
                if cells_matrix[i - 1][j] == 1:
                    cells += 1
            if i > 0 and j < (columns - 1):
                if cells_matrix[i - 1][j + 1] == 1:
                    cells += 1
            if j < (columns - 1):
                if cells_matrix[i][j + 1] == 1:
                    cells += 1
            if i < (lines - 1) and j < (columns - 1):
                if cells_matrix[i + 1][j + 1] == 1:
                    cells += 1
            if i < (lines - 1):
                if cells_matrix[i + 1][j] == 1:
                    cells += 1
            if i < (lines - 1) and j > 0:
                if cells_matrix[i + 1][j - 1] == 1:
                    cells += 1
            if j > 0:
                if cells_matrix[i][j - 1] == 1:
                    cells += 1

            column.append(cells)

        line.append(column)

    for i in range(lines):
        for j in range(columns):
            if cells_matrix[i][j] == 1:
                if line[i][j] < 2 or line[i][j] > 3:
                    cells_matrix[i][j] = 0
                    board_cells.remove((i, j))
            if cells_matrix[i][j] == 0:
                if line[i][j] == 3:
                    cells_matrix[i][j] = 1
                    board_cells.append((i, j))
