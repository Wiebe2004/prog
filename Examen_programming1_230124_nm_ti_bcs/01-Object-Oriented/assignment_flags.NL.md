# Examenvraag 1: Flags

* Plaats alle code voor deze oefening in `flags.py`.
* In deze instructies zullen we altijd `self` weglaten.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een `basic_tests_flags.py` bestand ontvangen dat basistesten bevat, zoals of bepaalde klassen bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_tests_flags.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich op die klasse richten worden overgeslagen.
    Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit.
    Het niet slagen/overslaan van tests betekent dat je code zeker incompleet of incorrect is.
    Maar geslaagde tests betekenen niet dat je code volledig correct is!
  * Dit testbestand moet correct uitgevoerd kunnen worden om punten te verdienen.

## Klasse Flag
De klasse `Flag` vertegenwoordigt nationale vlaggen. Omwille van de eenvoud worden hier alleen gestreepte vlaggen beschouwd. Er hoeft geen rekening gehouden te worden met emblemen of andere ontwerpen.

* Definieer een klasse `Flag`.
* Definieer de constructor van `Flag`:
    * De constructor neemt drie parameters: `country` (een string), `colors` (een tuple van kleuren die op de vlag worden getoond), en `horizontal` (een boolean: True als de strepen horizontaal zijn en False als de strepen verticaal zijn).
    * De tuple `colors` is een geordende reeks die de rangschikking van de kleuren op de vlag aangeeft. Een kleur kan meer dan eens op dezelfde vlag voorkomen.
    * Voorbeelden:
        * `country = "Belgium"`; `belgian_colors = ("black","yellow","red")`; `horizontal = False`
        * `country = "Germany"`; `german_colors = ("black","red","yellow")`; `horizontal = True`
        * `country = "Spain"`; `spanish_colors = ("red","yellow","red")`; `horizontal = True`
* Sla `country` en `horizontal` op in public fields.
* Sla `colors` op in een private field dat beschikbaar is via een property.
* Definieer een setter voor `colors`.
  * Een vlag moet ten minste één kleur bevatten. Als de tuple van kleuren ontbreekt of leeg is, moet de setter een `ValueError` oproepen.
* Definieer een methode `get_info()` die een tekenreeksrepresentatie van de vlag teruggeeft, zoals hieronder getoond.

## Klasse Parade
De klasse `Parade` vertegenwoordigt een gebeurtenis waarbij een opeenvolging van vlaggen wordt weergegeven.
* Definieer een klasse `Parade`.
* Definieer de constructor van `Parade`:
    * De constructor neemt één parameter: `name` (een string).
    * Een `Parade` bevat ook een veld `flags` dat een lijst is van `Flag`'s die worden weergegeven. Deze lijst is leeg wanneer een `Parade` wordt aangemaakt.
* Sla `name` op in een public field.
* Sla `flags` op in een private field dat toegankelijk is via een property.
* Definieer een methode `add_flag(flag)` die `flag` toevoegt aan `flags`.
  * Een `Flag` mag niet toegevoegd worden wanneer er al een `Flag` voor het betreffende land in de lijst staat. Bij de controle of 2 landen hetzelfde zijn, hou je geen rekening met hoofdletters. 
* Definieer een methode `remove_flag(country)` die een `Flag` verwijdert uit `flags`, gebaseerd op het opgegeven land. Als de vlag van dit land niet in `flags` staat, doe dan niets. Bij de controle of 2 landen hetzelfde zijn, hou je geen rekening met hoofdletters. 
* Zowel `add_flag(flag)` als `remove_flag(country)` veranderen eventueel de waarde van het veld `flags` maar geven niets terug.

## Voorbeeldgebruik

```python
>>> belgian_flag = Flag("Belgium",("black","yellow","red"),False)
>>> german_flag = Flag("Germany",("black","red","yellow"),True)
>>> spanish_flag = Flag("Spain",("red","yellow","red"),True)
>>> dutch_flag = Flag("Netherlands",("red","white","blue"),False)

>>> erasmus_parade = Parade("Erasmus Parade")

>>> erasmus_parade.add_flag(belgian_flag)
>>> erasmus_parade.add_flag(german_flag)
>>> erasmus_parade.add_flag(spanish_flag)
>>> erasmus_parade.add_flag(dutch_flag)

>>> erasmus_parade.remove_flag("netherlands")

>>> for flag in erasmus_parade.flags:
        print(flag.get_info())

Flag of Belgium
Colors: black yellow red
Orientation: vertical
Flag of Germany
Colors: black red yellow
Orientation: horizontal
Flag of Spain
Colors: red yellow red
Orientation: horizontal
```
