# Exam Question 1: Flags

* Place all code for this exercise in `flags.py`.
* In these instructions we will always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure to get the names exactly right, even those of the parameters.
* You have received a `basic_tests_flags.py` file which contains basic testing, like if certain classes exist and if you've used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests_flags.py
    ```

  * A missing class will cause tests focusing on that class to be skipped.
    Skipped tests therefore still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests means that your code is definitely incomplete or incorrect.
    But passed tests do not mean that your code is fully correct!
  * This test file must be able to run correctly to earn credit.

## Class Flag
The class `Flag` represents national flags. For simplicity's sake, only striped flags are considered here. No emblems or other designs need to be taken into account.

* Define a class `Flag`.
* Define `Flag`'s constructor:
    * The constructor takes three parameters: `country` (a string), `colors` (a tuple of colors that are shown on the flag), and `horizontal` (a boolean: True in case the stripes are horizontal and False in case the stripes are vertical).
    * The tuple `colors` is an ordered sequence indicating the arrangement of the colors as they appear on the flag. A color may appear more than once on the same flag.
    * Examples:
        * `country = "Belgium"`; `belgian_colors = ("black","yellow","red")`; `horizontal = False`
        * `country = "Germany"`; `german_colors = ("black","red","yellow")`; `horizontal = True`
        * `country = "Spain"`; `spanish_colors = ("red","yellow","red")`; `horizontal = True`
* Store `country` and `horizontal` in public fields.
* Store  `colors` in a private field available via a property.
* Define a setter for `colors`.
  * A flag must contain at least one color. If the tuple of colors is missing or empty, the setter should raise a `ValueError`.
* Define a method `get_info()` which returns a string representation of the flag, as shown below.

## Class Parade
The class `Parade` represents an event where a sequence of flags will be displayed.
* Define a class `Parade`.
* Define `Parade`'s constructor:
    * The constructor takes one parameter: `name` (a string).
    * A `Parade` also includes a field `flags` which is a list of `Flag`'s which will be displayed. This list is empty when a `Parade` is being created.
* Store `name` in a public field.
* Store `flags` in a private field which can be accessed via a property.
* Define a method `add_flag(flag)` which adds `flag` to `flags`.
  * A `Flag` should not be added if a `Flag` for that particular country is already present in the list. While checking wheter 2 countries have the same name, you ignore capital letters.
* Define a method `remove_flag(country)` which removes a `Flag` from `flags`, based on the country provided. If this country's flag is not in `flags`, do nothing. While checking wheter 2 countries have the same name, you ignore capital letters.
* Both `add_flag(flag)` and `remove_flag(country)` possibly change the value of the field `flags` but do not return anything.

## Example usage

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
