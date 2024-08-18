# Exam Question 3: Cities

* You have received python code in the `cities.py` file. You will need to correct the code found in this file. Make a file `cities_corrected.py` to correct the code.
* Make sure to get the names exactly right, even those of the parameters. In this case, this means don't change the names that have been provided in the `cities.py` file.
* There are no basic pytests for this exercise.
 
  
## Background Information

* We've attempted an implementation based on the problem description below. You can find this code in `cities.py`. Unfortunately, it's not working as expected. Your task is to correct the code so it runs according to the rules described here.

    * Cities
        * Take three cities as an example: Antwerp, Brussels, and Leuven.
          * The distance between Leuven and Antwerp is 60 km.
          * The distance between Leuven and Brussels is 30 km.
          * The distance between Antwerp and Brussels is 50 km.
        * We propose representing these distances in a matrix like the one shown here:

          |          | Antwerp | Brussels | Leuven |
          |----------|-----------|---------|--------|
          | **Antwerp**|    0      |   50    |   60   |
          | **Brussels** |   50      |    0    |   30   |
          | **Leuven**   |   60      |   30    |    0   |

        * Notice that the elements on the diagonal are always 0: the distance between Antwerp and Antwerp is naturally 0.
        * Also, distances are symmetric: the distance from Brussels to Leuven is 30 and the distance from Leuven to Brussels is also 30.
        * In python, we can represent this matrix with a 2D-list (a list of lists), for example:
          * distances = [[0,50,60],[50,0,30],[60,30,0]]
        * Then to find the distance between Brussels and Leuven, we know that Brussels is the 2nd element (index = 1) and Leuven is the third element (index = 2), so distances[1][2] = 30 (the distance between Brussels and Leuven). distances[2][1] = 30 (the distance between Leuven and Brussels), because the distances are symmetric.

    * The program is intended include the following functionalities:
        * `is_valid_distance_matrix(nss)`:
          * this function should check if the given 2D list, `nss`, is a valid distance matrix:
              * it should be square: with the same number of rows and columns
              * the diagonal values should always be 0
              * it should be symmetrical, so nss[i][j] is equal to nss[j][i]
              * there must be at least 1 element
        * `total_distance(distances,cities,itinerary)`
          * given `distances` - a distance matrix, `cities` - a list of city names, and `itinerary` a list of city names that forms a trip, this function should calculate the total distance traveled
            * Example: an itinerary [a, b, c] should add the distance from a to b and the distance from b to c
          * In case something is not valid, return -1:
            * a particular city in the itinerary is not in the list of cities: invalid
            * the distance matrix is not valid: invalid
          * A visit to a single city should return a distance of 0


## Example usage


* Valid Distance Matrices:

    |    0      |   1    |   2  |
    |---|---|---|
    |  **1**    |   **0**   |   **3**  |
    |   **2**   |   **3**   |   **0**  |


    |    0      |  2    |
    |---|---|
    |  **2**    |   **0**   | 


    |    0      |   1    |   1  |  1  |
    |---|---|---|---|
    |  **1**   |   **0**   |   **1**  |   **1**  |
    |  **1**   |   **1**   |   **0**  |   **1**  |
    |  **1**   |   **1**   |   **1**  |   **0**  |

* Invalid Distance Matrices


    |    0      |   2    |   3  |
    |---|---|---|
    |  **2**    |   **0**   |   **4**  |
    |  **3**    |   **4**   |   **0**  |
    |   **3**   |   **6**   |   **7**  |


    |    1      |  2    |
    |---|---|
    |  **2**    |   **1**   | 


    |    0      |   1    |   1  |  1  |
    |---|---|---|---|
    |  **5**   |   **0**   |   **1**  |   **1**  |
    |  **1**   |   **1**   |   **0**  |   **1**  |
    |  **1**   |   **1**   |   **1**  |   **0**  |




```python
>>> distances1 = [[0,1],[1],[0]]
>>> distances2 = [[]]
>>> distances3 = []
>>> distances4 = [[0]]
>>> distances5 = [[1,2]]
>>> distances6 = [[0,1,1],[1,0,1],[1,1,0]]
>>> distances7 = [[0,5,6,1],[5,2,1,1],[6,1,0,7],[1,1,7,0]]
>>> distances8 = [[0,5,6,1],[5,2,1,1],[6,1,0,7]]

>>> is_valid_distance_matrix(distances1)
False

>>> is_valid_distance_matrix(distances2)
False

>>> is_valid_distance_matrix(distances3)
False

>>> is_valid_distance_matrix(distances4)
True

>>> is_valid_distance_matrix(distances5)
False

>>> is_valid_distance_matrix(distances6)
True

>>> is_valid_distance_matrix(distances7)
False

>>> is_valid_distance_matrix(distances8)
False

>>> matrix1 = [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
>>> cities1 = ["a","b","c","d"]
>>> itinerary1 = ["a","b","c","d","c","b","a"]

>>> total_distance(matrix1,cities1,itinerary1)
22

>>> matrix2 = [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]]
>>> cities2 = ["a","b","c","d"]
>>> itinerary2 = ["a","x","c"]

>>> total_distance(matrix2,cities2,itinerary2)
-1


>>> distances3 = [[0,1],[1,0]]
>>> cities3 = ["a","b"]
>>> itinerary3 = []

>>> total_distance(distances3,cities3,itinerary3)
0
```

## Your Task: Bug Squashing

* Find and fix the bugs you find in `cities.py`.
