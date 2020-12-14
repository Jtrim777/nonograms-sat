from pysat.formula import CNF


def reduce_board(size: int, rows: [[int]], cols: [[int]]):
    """Reduces the the description of a Nonogram puzzle to a CNF formula

    :param size: The number of cells in each row/column
    :param rows: The hints for each row
    :param cols: The hints for each column
    :return: A CNF object representing the board's possible solutions
    """
    clauses = []

    base = size * size
    for i, row in enumerate(rows):
        uvars = [j+(i*size)+1 for j in range(size)]
        reduction = reduce_set(size, row, uvars, base)
        clauses += reduction.clauses
        base += len(reduction.auxvars)

    for i, col in enumerate(cols):
        uvars = [i+(j*size)+1 for j in range(size)]
        reduction = reduce_set(size, col, uvars, base)
        clauses += reduction.clauses
        base += len(reduction.auxvars)

    cnf = CNF()
    for clause in clauses:
        cnf.append(clause)

    return cnf


def reduce_set(cells: int, blocks: [int], uvars: [int], nbase: int):
    """Produces a CNF-represented DNF which holds all the possible combinations for a row/col

    :param cells: The length of the row/col
    :param blocks: The hints for this row/col
    :param uvars: The literals to use for variables in this clause
    :param nbase: The base index for the auxiliary variables
    """
    combos = []

    if sum(blocks) + (len(blocks) - 1) > cells:
        raise Exception("The passed block values exceeded the number of cells")

    ogcombo = []
    acc = 0
    for block in blocks:
        ogcombo.append(acc)
        acc += block + 1

    combos.append(ogcombo)

    ccombo = ogcombo.copy()

    lookat = len(blocks) - 1
    while lookat >= 0:
        if blocks[-1] + ccombo[-1] < cells:
            ccombo[lookat] = ccombo[lookat] + 1
            s = ccombo[lookat] + blocks[lookat] + 1
            for i in range(lookat + 1, len(blocks)):
                ccombo[i] = s
                s += blocks[i] + 1
            lookat = len(blocks) - 1
            combos.append(ccombo.copy())
        else:
            lookat -= 1
            s = ccombo[lookat] + blocks[lookat] + 1
            for i in range(lookat + 1, len(blocks)):
                ccombo[i] = s
                s += blocks[i] + 1

    cnf = CNF()
    for combo in combos:
        clause = [-v if in_combo(i, combo, blocks) else v for i, v in zip(range(cells), uvars)]
        cnf.append(clause)

    return cnf.negate(nbase)


def in_combo(i, combo, sizes):
    """Determines if a certain cell is true in a particular combination

    :param i: The cell to test
    :param combo: The combination
    :param sizes: The length of the row/coll
    :return: A boolean value indicating the cell's state in this combo
    """
    for c, z in zip(combo, sizes):
        if c <= i < c+z:
            return True

    return False


