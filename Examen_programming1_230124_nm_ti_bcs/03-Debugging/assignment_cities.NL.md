# Exam Question 3: Cities

* Verbeter de code die je vindt in het bestand `cities.py`. Maak hiervoor een nieuw bestand `cities_corrected.py` waar je jouw verbeterde code plaatst.
* Zorg ervoor dat de de namen die je gebruikt volledig correct zijn, zowel deze van de functies als die van de parameters. Bij deze oefening mag je de gebruikte namen in het bestand `cities.py` dus niet veranderen. 
* Er zijn daarom ook geen basis pytests voorzien.



## Background Information


* Hieronder vind je een probleemomschrijving. In het bestand `cities.py` vind je onze poging om de opdracht op te lossen. Helaas werkt de code niet zoals verwacht. Het is nu aan jou om de code te verbeteren zodat deze foutloos werkt en voldoet aan de eisen zoals beschreven in de opgave. 

    * Cities
        * We gebruiken 3 steden (cities) als voorbeeld: Antwerp, Brussels, and Leuven.
          * De afstand tussen Leuven en Antwerp is 60 km.
          * De afstand tussen Leuven en Brussels is 30 km.
          * De afstand tussen Antwerp en Brussels is 50 km.
        * We stellen deze afstanden voor in een matrix: 

          |          | Antwerp | Brussels | Leuven |
          |----------|-----------|---------|--------|
          | **Antwerp**|    0      |   50    |   60   |
          | **Brussels** |   50      |    0    |   30   |
          | **Leuven**   |   60      |   30    |    0   |

        * De getallen diagonaal in de matrix zijn steeds 0: de afstand tussen Antwerp en Antwerp is uiteraard 0.
        * De afstandsmatrix is ook symmetrisch: de afstand van Brussels tot Leuven is 30, de afstand van Leuven tot Brussels is eveneens 30.
        * In python stellen we deze matrix voor met een 2D-list (een list of lists), bijvoorbeeld:
          * distances = [[0,50,60],[50,0,30],[60,30,0]]
        * Om de afstand van Brussles tot Leuven te vinden, doen we het volgende: Brussels is het 2e element (index = 1) en Leuven het derde (index = 2), dus distances[1][2] = 30 (afstand tussen Brussels en Leuven) en distances[2][1] = 30 (afstand tussen Leuven en Brussels), beide afstanden zijn gelijk omdat ze symmetrisch zijn. 
        

    * Het programma moet volgende functionaliteiten bevatten:
        * `is_valid_distance_matrix(nss)`:
          * deze functie controleert of de gegeven 2D-lijst `nss`, een correcte afstandsmatrix is:
              
              * Het aantal rijen moet gelijk zijn aan het aantal kolommen.
              * De diagonale waardes moeten altijd 0 zijn.
              * De matrix moet symmetrisch zijn, dit betekent dat nss[i][j] gelijk is aan nss[j][i]
              * De matrix moet tenminste 1 element bevatten
        * `total_distance(distances,cities,itinerary)`
          * Deze functie berekent de totale afgelegde afstand op basis van volgende gegevens: `distances`: een afstandsmatrix, `cities`: een lijst met namen van steden en `itinerary`: een lijst met namen van steden die een route vormen.
            * Bijvoorbeeld: de route [a, b, c] telt de afstand van a to b op bij de afstand van b tot c.
          * Bij foutieve inputdata, geeft de functie -1 terug (return):
            * een stad op de route komt niet voor in de lijst met steden: fout
            * de afstandsmatrix is geen correcte afstandsmatrix: fout
          * Een bezoek aan één stad moet een afstand van 0 teruggeven


## Example usage


* Correcte afstandsmatrices:

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

* Incorrecte afstandsmatrices


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

* Zoek en verbeter de fouten in `cities.py` zodat de code werkt zoals gevraagd.
