def make_board(size):
    """Cria as linhas no eixo x e y"""
    width, height = size
    lines_x = [[(0, y), (width, y)] for y in range(11, height, 12)]
    lines_y = [[(x, 0), (x, height)] for x in range(11, width, 12)]

    return (lines_x, lines_y)


def make_cells_matrix(cells_matrix, lines, columns):
    """ Cria uma matriz com todos os quadrados do tabuleiro com o valor 0.
        Onde zero significa vazio e 1 significa ocupado
    """
    for i in range(0, len(lines)):
        col = []
        for j in range(0, len(columns)):
            col.append(0)

        cells_matrix.append(col)