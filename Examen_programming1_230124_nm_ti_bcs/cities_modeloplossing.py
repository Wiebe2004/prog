### means you had to adapt the code on that line
# extra information

def is_valid_distance_matrix(nss):
    if len(nss) == 0:   ### When the distance matrix is empty, it is not a valid one. The given code len(nss[0]) checks the len of the first row. It throws an index error if nss is empty.
        return False
    for i in range(len(nss)): 
        if len(nss[i]) != len(nss): #checks whether the length of each row equals the number of rows (NxN matrix)
            return False # if not, return False
        for j in range(len(nss[i])): 
            if nss[i][j] != nss[j][i]: ### checks the symmetry of the matrix, whether the value on row i, col j is the same as the value on row j, col i. Antwerp - Brussels vs Brussels - Antwerp. The given code, nss[i][j]!= nss[i][j] checks if a cell is different from itself...
                return False
        if nss[i][i] != 0: ### the values on the diagonal should be 0.
            return False    ### If not it is not a valid distance matrix. 
                            # The code said: if nss[i][i]==0, return True. This means that when one diagonal value == 0, it is a valid matrix... which is not the case.
    return True


def total_distance(distances,cities,itinerary):
    if not is_valid_distance_matrix(distances):
        return -1
    for city in itinerary: #For city in the itinerary
        if city not in cities: ### should be: if the city is not listed in cities... it does not make sense to check wheter it is part of the itinerary as it is a value you derived from itinerary.
            return -1
    if len(itinerary) == 1: ### if you only have one city, the distance of the itinerary is 0. 
        return 0
    total = 0 ### you should initiate the variable befor you can add a value to it. This gives an error.
    for destination in range(len(itinerary)-1): ### -1 added. We go from city to city. Below we define a start and end city (start: index = destination, end: index = destination +1. Therefore we should not include the last destination in the range, this causes an index error.
        for city in range(len(cities)): #looping over the cities in the list to define start and end city (index in the cities list, corresponding to the matrix indices)
            if itinerary[destination] == cities[city]: 
                start = city
            if itinerary[destination+1] == cities[city]:
                end = city
        total += distances[start][end] ### we check the distance from the start city to the end city (of the sub-trip) and add it to the total.
                                        #distances[city][destination], looks for the index of city (cities list) and destination (based on the itinerary), after the loop, meaning it will always give the highest index. When the itinerary is longer than the total number of cities, this gives an index error.
    return total
