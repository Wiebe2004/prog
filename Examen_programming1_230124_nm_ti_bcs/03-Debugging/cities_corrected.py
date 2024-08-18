def is_valid_distance_matrix(nss):
    # diagonal = 0
    if len(nss) == 0 :
        return False
    for i in range(len(nss)):
        if len(nss[i]) != len(nss):
            return False
        for j in range(len(nss[i])):
            if nss[i][j] != nss[j][i]:
                return False
        if nss[i][i] != 0:
            return False
    return True


def total_distance(distances, cities, itinerary):
    if not is_valid_distance_matrix(distances):
        return -1
    for city in itinerary:
        if city not in cities:
            return -1
    if len(itinerary) == 0:
        return 0
    total = 0
    for destination in range(len(itinerary)-1):
        for city in range(len(cities)):
            if itinerary[destination] == cities[city]:
                start = city
            if itinerary[destination + 1] == cities[city]:
                end = city
        total += distances[start][end]
    return total


distances1 = [[0, 1], [1], [0]]
distances2 = [[]]
distances3 = []
distances4 = [[0]]
distances5 = [[1, 2]]
distances6 = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
distances7 = [[0, 5, 6, 1], [5, 2, 1, 1], [6, 1, 0, 7], [1, 1, 7, 0]]
distances8 = [[0, 5, 6, 1], [5, 2, 1, 1], [6, 1, 0, 7]]

print(is_valid_distance_matrix(distances1))


print(is_valid_distance_matrix(distances2))


print(is_valid_distance_matrix(distances3))


print(is_valid_distance_matrix(distances4))


print(is_valid_distance_matrix(distances5))


print(is_valid_distance_matrix(distances6))


print(is_valid_distance_matrix(distances7))


print(is_valid_distance_matrix(distances8))

matrix1 = [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
cities1 = ["a","b","c","d"]
itinerary1 = ["a","b","c","d","c","b","a"]

print(total_distance(matrix1,cities1,itinerary1))

matrix2 = [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
cities2 = ["a","b","c","d"]
itinerary2 = ["a","x","c"]

print(total_distance(matrix2,cities2,itinerary2))

distances3 = [[0,1],[1,0]]
cities3 = ["a","b"]
itinerary3 = []

print(total_distance(distances3,cities3,itinerary3))