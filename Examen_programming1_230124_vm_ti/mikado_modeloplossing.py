### means you had to adapt the code on that line
# extra information

def remove_stick_if_possible(matrix, i):
    idx = i - 1 ### the sticks are numbered from 1 to x. Indices start at 0. Therfore -1. Errorcodes: When checking for the stick with the highest number, an error occurs: list index out of range.
    for row in matrix:
        if row[idx] == True: ### True means a stick lays on top of the stick we are checking, so we return the matrix if row[idx] == True.
            return matrix
    for j in range(len(matrix[idx])): ### for j in matrix[idx] would mean loping over a single value True or False. We want to change every value of the row to False (when removing a stick, it does not lay on any other stick.) 
        matrix[idx][j] = False          # Therefore we are interested in the len of that row, so we can loop over the indices.
    return matrix  


def is_valid_strategy(matrix, ns):
    if len(ns) > 0: ### ns[0] takes the first item of ns and checks wheter its > 0. This throws an indexerror when ns is empty. In the code inside the if statement, we want to check if a stick can be removed, therefore ns should contain stick indices.
        i = ns[0]
        idx = i-1 ### same as the function above, stick numbers start at 1, matrix/list indeces at 0. Therfore idx = i - 1. 
        for row in matrix:
            if row[idx] == True: ### same as the function above, row[idx] == True, means a stick is laying on the stick we are checking. If that is the case, the strategy is not valid, return False.
                return False
        newmatrix = remove_stick_if_possible(matrix, i) ### With the function above we generate the new matrix when removing the stick. The function takes as argument i (stock number), not the list/matrix index.
        ns.pop(0) 
        return is_valid_strategy(newmatrix,ns)
    else:  #when ns is empty
        for k in matrix: #for every row in the matrix
            for j in k: #for every value in the row
                if j == True: ### if that value == True meaning a stick is laying on top of another, meaning the game is not finished.
                    return False ### False, ge game is not finished
        return True #If ns is empty and all values of the matrix == False, it is a valid strategy.

