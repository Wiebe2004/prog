# Examenvraag 2: Studentgegevens

* Plaats alle code voor deze oefening in `studentdata.py`.
* Zorg ervoor dat de de namen die je gebruikt volledig correct zijn, zowel deze van de functies als die van de parameters.
* Er is een testbestand `basic_tests_studentdata.py` voorzien die test of bepaalde classes of functies bestaan en of je de correcte namen hebt gebruikt.

  * Gebruik volgend commando om de testen te laten lopen:

    ```bash
    $ pytest basic_tests_studentdata.py
    ```

  * Als er een klasse ontbreekt, zal de test van die klasse worden overgeslagen. Testen die worden overgeslagen worden beschouwd als 'failed'.
  * De testen controleren enkel oppervlakkig. Een test die faalt of wordt overgeslagen betekent dat jouw code sowieso fout of incompleet is. Als alle testen slagen, wil dit niet zeggen dat je code volledig juist is, het geeft enkel aan dat je de correcte benamingen hebt gebruikt.
  * Als dit testbestand niet foutloos loopt, verdien je sowieso geen punten.


## Studentengegevens verwerken

Je hebt een tekstbestand genaamd `studentdata.txt` ontvangen met de volgende opmaak:

```plaintext
Jef, Wiskunde, 11
Tom, Chemie, 9
Jef, Chemie, 8
Jef, Biologie, 16
Tom, Biologie, 17
An, Fysica, 14
An, Wiskunde, 13
```

### Schrijf enkele Python-functies om deze gegevens te verwerken, volgens de volgende vereisten:

* Definieer een functie `calculate_average(grades)` die als parameter een dictionary met als key een naam en als value een lijst van cijfers krijgt, en een nieuwe dictionary teruggeeft met als key dezelfde naam en als value het gemiddelde cijfer per naam, afgerond op één cijfer na de komma. Je kunt het gemiddelde berekenen door de individuele cijfers op te tellen en te delen door het aantal cijfers.
* Definieer een functie `calculate_stats(input)` die de naam van een tekstbestand als invoer neemt en het als volgt verwerkt:
    * Opent het tekstbestand dat als invoer gegeven wordt en leest de leerlingen, vakken en cijfers in. Je kan aannemen dat dit het patroon volgt dat hierboven getoond wordt. Sla de informatie op in meerdere dictionaries:
      * by_course: `course_name` als key en een lijst van `grades` behaald in die cursus als value
      * by_student: `student_name` als key en een lijst van `grades` behaald per student als value
    * Gebruik de functie die je hierboven gedefinieerd hebt om het gemiddelde cijfer per cursus en het gemiddelde cijfer per student te vinden.
    * Schrijf de resultaten in een bestand genaamd `results.txt` volgens deze structuur:
        ```plaintext
        Per course:
          Wiskunde: 12.0
          Chemie: 8.5
          Biologie: 16.5
          Fysica: 14.0
        Per student:
          Jef: 11.7
          Tom: 13.0
          An: 13.5
        ```
