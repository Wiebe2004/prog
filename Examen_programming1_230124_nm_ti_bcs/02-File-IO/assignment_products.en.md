# Exam Question 2: Products

* Place all code for this exercise in `products.py`.
* Make sure to get the names exactly right, even those of the parameters.
* You have received a `basic_tests_products.py` file which contains basic testing, like if certain classes exist and if you've used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests_products.py
    ```

  * A missing class will cause tests focusing on that class to be skipped.
    Skipped tests therefore still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests means that your code is definitely incomplete or incorrect, but passed tests do not mean that your code is fully correct!
  * This test file must be able to run correctly to earn credit.

## Processing Product Data

You have received a text file called `products.txt` with the following formatting:

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

### Write Python code to process this data, according to the following requirements:

* Define a function `calculate_average(products)` that takes as parameter a dictionary containing products and their price and returns the total average price rounded to an integer value. 
    * You can calculate the average by adding up the prices of the products and dividing by the number of products.
* Define a function `most_expensive(products)` that takes as parameter a dictionary containing products and their price and returns a list with the most expensive product. If multiple products have the same highest price, the list contains the names of all these products.
* Define a function `calculate_stats(input)` that takes as input the name of a text file and processes it as follows:
    * It opens the text file given as input and reads in the products and prices. You can assume it follows the pattern shown above. Store the information in a dictionary where each entry has a `name` and `price`.
    * Use the functions you've defined above to find the average price and most expensive products.
    * Write the results to a file called `results.txt` according to the following format:
        ```plaintext
        Total number of products: 7
        Average price: 471
        Most expensive products:
            Laptop
            Television
        ```
