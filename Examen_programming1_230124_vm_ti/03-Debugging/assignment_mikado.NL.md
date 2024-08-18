# Exam Question 3: Mikado

* Verbeter de code die je vindt in het bestand `mikado.py`. Maak een nieuw bestand `mikado_corrected.py`waar je jouw verbeterde code plaatst.
* Zorg ervoor dat de de namen die je gebruikt volledig correct zijn, zowel deze van de functies als die van de parameters. Bij deze oefening mag je de gebruikte namen in het bestand `mikado.py` dus niet veranderen. 
* Er zijn daarom ook geen basis pytests voorzien.

## Background Information

* Hieronder vind je een probleemomschrijving. In het bestand `mikado.py` vind je onze poging om de opdracht op te lossen. Helaas werkt de code niet zoals verwacht. Het is nu aan jou om de code te verbeteren zodat deze foutloos werkt en voldoet aan de eisen zoals beschreven in de opgave. 


Mikado is een twee speler spel waarbij een aantal stokjes op een hoopje op tafel liggen. Een speler moet voorzichtig proberen een stokje naar keuze van deze stapel te halen, zonder daarbij de andere stokjes te verroeren. Zolang die hierin slaagt, mag die stokjes blijven verzamelen. Indien de speler echter wel een andere stokje laat bewegen, is het de beurt van de andere speler om zoveel mogelijk stokjes op te pakken. Zo blijven de spelers elkaar afwisselen tot er geen stokjes meer overblijven. Degene die de meeste stokjes heeft, wint.

Om dit te implementeren, moeten we de ligging van de stokjes kunnen voorstellen in code. We doen dit door elk stokje te nummeren, beginnend met 1. Vervolgens gaan we na welk stokje bovenop welk ander stokje ligt. Merk op dat een stokje op 0, 1, of meerdere andere stokjes kan liggen. Om deze informatie voor te stellen, maken we gebruik van een N × N matrix, waarbij N het aantal stokjes voorstelt. Indien stokje i rechtstreeks op stokje j ligt (d.i. beide stokjes raken elkaar aan, en i ligt bovenop j), dan bevat de matrix op rij i en kolom j de waarde True, zoniet False.

Bijvoorbeeld, stel dat N = 3. Stokje 1 ligt onderaan, hierop ligt stokje 2, en op beide ligt stokje 3. We kunnen dit anders verwoorden als volgt:  
* Stokje 1 (rij 1) ligt niet op stokje 1 (kolom 1), niet op stokje 2 (kolom 2) en niet op stokje 3 (kolom 3)
* Stokje 2 (rij 2) ligt wel op stokje 1 (kolom 1), niet op stokje 2 (kolom 2) en niet op stokje 3 (kolom 3)
* Stokje 3 (rij 3) ligt wel op stokje 1 (kolom 1), wel op stokje 2 (kolom 2) en niet op stokje 3 (kolom 3)

(Merk op dat een stokje niet op zichzelf ligt.) We stellen dit voor door volgende matrix:

| False    | False     | False     |
|----------|-----------|-----------|
| **True** | **False** | **False** |
| **True** | **True**  | **False** |


Deze matrix wordt in Python voorgesteld door een 2D-list (list- of lists), bovenstaand voorbeeld geeft dan: 

[ [False, False, False], [True, False, False], [True, True, False] ]

* Het programma moet volgende functionaliteiten omvatten:
    * Schrijf een functie `remove_stick_if_possible(matrix, i)` die
        * indien stokje i niet vrij is, de matrix ongewijzigd teruggeeft.
        * indien stokje i wel vrij is, een nieuwe matrix teruggeeft gelijk aan de matrix maar waarbij stokje i op geen enkel ander stokje meer ligt. Het wordt met andere woorden van de hoop verwijderd en apart gelegd. De grootte van de matrix blijft ongewijzigd (NxN).
        

    * Schrijf een recursieve functie `is_valid_strategy(matrix, ns)` die 
        * gegeven een matrix `matrix` en een rij stokindices `ns`, nagaat of de stokjes kunnen verwijderd worden in de volgorde aangegeven door ns, d.i. te allen tijde mogen enkel vrije stokjes weggehaald worden. 
        * Ook moeten na het weghalen van alle opgesomde stokjes alle stokjes vrij zijn. 
        * Je kan er van uit gaan dat alle getallen in de lijst `ns` stokindices zijn van de gegeven matrix. Dat wil zeggen dat, gegeven een NxN matrix alle getallen in `ns` <= N.
        * Ter info: een recursieve functie is een functie die naar zichzelf verwijst.
        


## Example usage

* Indien alle stokjes reeds vrij zijn in de beginsituatie, is [] een geldige strategie.
* Indien stokje 1 op 2 ligt, is [1, 2] geldig, naar [2, 1] niet.

```python
>>> matrix1 = [[False, False], [True, False]]
>>> matrix2 = [[False, True], [True, False]]
>>> matrix3 = [[False, True], [True, False]]
>>> matrix4 = [[False, False], [True, False]]
>>> matrix5 = [[False, False, False], [False, False, False], [False, False, False]]
>>> matrix6 = [[False, True, True], [False, False, False], [False, False, False]]
>>> matrix7 = [[False, False, False], [True, False, False], [False, False, False]]
>>> matrix8 = [[False, False, True], [True, False, False], [False, False, False]]
>>> matrix9 = [[False, False, True], [True, False, True], [True, False, False]]

>>> remove_stick_if_possible(matrix1,1)
[[False, False], [True, False]]

>>> remove_stick_if_possible(matrix2,1)
[[False, True], [True, False]]

>>> remove_stick_if_possible(matrix3,2)
[[False, True], [True, False]]

>>> remove_stick_if_possible(matrix4,2)
[[False, False], [False, False]]

>>> remove_stick_if_possible(matrix5,1)
[[False, False, False], [False, False, False], [False, False, False]]

>>> remove_stick_if_possible(matrix6,1)
[[False, False, False], [False, False, False], [False, False, False]]

>>> remove_stick_if_possible(matrix7,1)
[[False, False, False], [True, False, False], [False, False, False]]

>>> remove_stick_if_possible(matrix8,1)
[[False, False, True], [True, False, False], [False, False, False]]

>>> remove_stick_if_possible(matrix9,2)
[[False, False, True], [False, False, False], [True, False, False]]
```

```python
>>> matrix10 = [[False, False], [False, False]]
>>> ns10 = []

>>> matrix11 = [[False, False], [False, False]]
>>> ns11 = [2]

>>> matrix12 = [[False, False], [False, False]]
>>> ns12 = [2, 1]

>>> matrix13 = [[False, True, False], [False, False, False], [False, False, False]]
>>> ns13 = [2, 1, 3]

>>> matrix14 = [[False, True, True], [False, False, True], [False, False, False]]
>>> ns14 = [1, 2]

>>> matrix15 = [[False, True], [False, False]]
>>> ns15 = []

>>> matrix16 = [[False, True], [False, False]]
>>> ns16 = [1, 2]


>>> is_valid_strategy(matrix10, ns10)
True

>>> is_valid_strategy(matrix11, ns11)
True

>>> is_valid_strategy(matrix12, ns12)
True

>>> is_valid_strategy(matrix13, ns13)
False

>>> is_valid_strategy(matrix14, ns14)
True

>>> is_valid_strategy(matrix15, ns15)
False

>>> is_valid_strategy(matrix16, ns16)
True
```

## Your Task: Bug Squashing
* Zoek en verbeter de fouten in `mikado.py` zodat de code werkt zoals gevraagd.
