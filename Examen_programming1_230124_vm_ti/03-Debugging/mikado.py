def remove_stick_if_possible(matrix, i):
    idx = i
    for row in matrix:
        if row[idx] == False:
            return matrix
    for j in matrix[idx]:
        matrix[idx][j] = False
    return matrix  

def is_valid_strategy(matrix, ns):
    if ns[0] > 0:
        i = ns[0]
        idx = i
        for row in matrix:
            if row[idx] == False:
                return False
        newmatrix = remove_stick_if_possible(matrix, idx)
        ns = ns[1:]
        return is_valid_strategy(newmatrix,ns)
    else:
        for k in matrix:
            for j in k:
                if j == False:
                    return True
        return True
    