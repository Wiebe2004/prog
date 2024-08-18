def remove_stick_if_possible(matrix, i):
    idx = i - 1
    for row in matrix:
        if row[idx] == True:
            return matrix
    for j in range(len(matrix[idx])):
        matrix[idx][j] = False
    return matrix


def is_valid_strategy(matrix, ns):
    if len(ns) > 0:
        i = ns[0]
        idx = i - 1
        for row in matrix:
            if row[idx] == True:
                return False
        newmatrix = remove_stick_if_possible(matrix, idx)
        ns.pop(0)
        return is_valid_strategy(newmatrix, ns)
    else:
        for k in matrix:
            for j in k:
                if j == True:
                    return False
        return True


matrix1 = [[False, False], [True, False]]
matrix2 = [[False, True], [True, False]]
matrix3 = [[False, True], [True, False]]
matrix4 = [[False, False], [True, False]]
matrix5 = [[False, False, False], [False, False, False], [False, False, False]]
matrix6 = [[False, True, True], [False, False, False], [False, False, False]]
matrix7 = [[False, False, False], [True, False, False], [False, False, False]]
matrix8 = [[False, False, True], [True, False, False], [False, False, False]]
matrix9 = [[False, False, True], [True, False, True], [True, False, False]]

print(remove_stick_if_possible(matrix1, 1))

print(remove_stick_if_possible(matrix2, 1))

print(remove_stick_if_possible(matrix3, 2))

print(remove_stick_if_possible(matrix4, 2))

print(remove_stick_if_possible(matrix5, 1))

print(remove_stick_if_possible(matrix6, 1))

print(remove_stick_if_possible(matrix7, 1))

print(remove_stick_if_possible(matrix8, 1))

print(remove_stick_if_possible(matrix9, 2))

matrix10 = [[False, False], [False, False]]
ns10 = []

matrix11 = [[False, False], [False, False]]
ns11 = [2]

matrix12 = [[False, False], [False, False]]
ns12 = [2, 1]

matrix13 = [[False, True, False], [False, False, False], [False, False, False]]
ns13 = [2, 1, 3]

matrix14 = [[False, True, True], [False, False, True], [False, False, False]]
ns14 = [1, 2]

matrix15 = [[False, True], [False, False]]
ns15 = []

matrix16 = [[False, True], [False, False]]
ns16 = [1, 2]


print(is_valid_strategy(matrix10, ns10))

print(is_valid_strategy(matrix11, ns11))

print(is_valid_strategy(matrix12, ns12))

print(is_valid_strategy(matrix13, ns13))

print(is_valid_strategy(matrix14, ns14))

print(is_valid_strategy(matrix15, ns15))

print(is_valid_strategy(matrix16, ns16))
