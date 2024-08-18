# Examenvraag 2: Products

* Schrijf je code voor deze oefening in het bestand `products.py`.
* Zorg ervoor dat de de namen die je gebruikt volledig correct zijn, zowel deze van de functies als die van de parameters.
* Er is een testbestand `basic_tests_products.py` voorzien die test of bepaalde classes of functies bestaan en of je de correcte namen hebt gebruikt.

  * Gebruik volgend commando om de testen te laten lopen:

    ```bash
    $ pytest basic_tests_products.py
    ```

  * Als er een klasse ontbreekt, zal de test van die klasse worden overgeslagen. Testen die worden overgeslagen worden beschouwd als 'failed'.
  * De testen controleren enkel oppervlakkig. Een test die faalt of wordt overgeslagen betekent dat jouw code sowieso fout of incompleet is. Als alle testen slagen, wil dit niet zeggen dat je code volledig juist is, het geeft enkel aan dat je de correcte benamingen hebt gebruikt.
  * Als dit testbestand niet foutloos loopt, verdien je sowieso geen punten.

## Verwerken van Productgegevens

Je krijgt een tekstbestand genaamd `products.txt` dat volgende informatie bevat:

```plaintext
Laptop, 800
Smartphone, 500
Tablet, 300
Headphones, 100
Camera, 600
Smartwatch, 200
Television, 800
...
```

### Schrijf Python code om deze data te verwerken op basis van onderstaande vereisten: 

* Schrijf een functie `calculate_average(products)`, met als parameter een dictionary die producten en hun bijhorende prijs bevat. De functie geeft de totale gemiddelde prijs, afgerond tot een geheel getal (integer), terug. 
    * Het gemiddelde bereken je door alle prijzen van de producten op te tellen en te delen door het aantal producten.
* Maak een functie `most_expensive(products)`, met als parameter een dictionary die producten en hun bijhorende prijs bevat. De functie geeft een lijst terug met het duurste product. Indien er meerdere producten de duurste zijn, d.w.z ze hebben dezelfde prijs, retourneert de functie een lijst met al deze producten.
* Definieer de functie `calculate_stats(input)`, met als parameter de naam van een tekstbestand. De functie doet het volgende:
    * Het opent een tekstbestand en leest de producten met hun prijzen in. Je kan ervan uitgaan dat de gegevens in het tekstbestand de structuur volgen zoals hierboven weergegeven. Bewaar de gegevens in een dictionary, waar elk item een `name` en `price` heeft. 
    * Gebruik de functies die je eerder schreef om de gemiddelde prijs te berekenen en het duurste product op te zoeken.
    * Schrijf je resultaten weg in een tekstbestand met de naam `results.txt`. Zorg ervoor dat je volgende structuur gebruikt:
        ```plaintext
        Total number of products: 7
        Average price: 471
        Most expensive products:
            Laptop
            Television
        ```
    

