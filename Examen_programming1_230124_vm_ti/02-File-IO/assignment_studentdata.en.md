# Exam Question 2: Student Data

* Place all code for this exercise in `studentdata.py`.
* Make sure to get the names exactly right, even those of the parameters.
* You have received a `basic_tests_studentdata.py` file which contains basic testing, like if certain classes exist and if you've used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests_studentdata.py
    ```

  * A missing class will cause tests focusing on that class to be skipped.
    Skipped tests therefore still count as failed.
  * The tests only perform superficial checks.
    Failing/skipped tests means that your code is definitely incomplete or incorrect.
    But passed tests do not mean that your code is fully correct!
  * This test file must be able to run correctly to earn credit.

## Processing Student Data

You have received text file called `studentdata.txt` with the following formatting:

```plaintext
Jef, Wiskunde, 11
Tom, Chemie, 9
Jef, Chemie, 8
Jef, Biologie, 16
Tom, Biologie, 17
An, Fysica, 14
An, Wiskunde, 13
```

### Write some Python functions to process this data, according to the following requirements:

1. Define a function `calculate_average(grades)` that takes as parameter a dictionary containing names as key and a list of grades as values and returns a new dictionary with the same names as key, and as value the average grade rounded to a single digit after the comma.
    * You can calculate the average by adding up the individual grades and dividing by the number of grades.
2. Define a function `calculate_stats(input)` which takes the name of a text file as input and processes it as follows:
    * Opens the text file given as input and read in the students, courses, and grades. You can assume it follows the pattern shown above. Store the information in multiple dictionaries:
      * by_course: `course_name` as key and a list of `grades` achieved in that course as value
      * by_student: `student_name` as key and a list of `grades` achieved per student as value
    * Use the function you've defined above to find the average grade per course and the  average grade per student.
    * Write the results to a file called `results.txt` according to the following format:
        ```plaintext
        Per Course:
          Wiskunde: 12.0
          Chemie: 8.5
          Biologie: 16.5
          Fysica: 14.0
        Per Student:
          Jef: 11.7
          Tom: 13.0
          An: 13.5
        ```
