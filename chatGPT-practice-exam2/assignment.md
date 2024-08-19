
---

### **Revised Question 1: Object-Oriented Programming - Book Collection Manager with Mixed Access Levels**

#### **Objective:**
You need to develop a system for managing a collection of books in a library. The system should allow users to add new books, retrieve information about existing books, and update book details. Additionally, you must use a combination of private, protected, and public attributes to encapsulate the book details.

#### **Requirements:**

1. **Class Design:**
   - Create a class `Book` with the following attributes:
     - `_title`: (protected) The title of the book (must be a non-empty string).
     - `author`: (public) The author of the book (must be a non-empty string).
     - `__year`: (private) The year the book was published (must be a positive integer).
   - Implement `@property` decorators for all attributes to enforce these constraints and to allow controlled access:
     - The `title` should be capitalized when retrieved and can be updated through a setter.
     - The `year` must always be a positive integer and can only be accessed or updated through a getter and setter.
   - Implement a method `get_info()` to return a string with the book's details.
   - Implement a method `update_info(title=None, author=None, year=None)` to update the book's details. Ensure that updates follow the constraints and that the `__year` attribute remains private.

2. **Collection Management:**
   - Create a class `Library` that manages a list of `Book` objects.
   - Implement methods to:
     - Add a new book to the library.
     - Remove a book by title.
     - Find a book by title and return its information using `get_info()`.
     - List all books by a specific author.

#### **Example Usage:**
```python
library = Library()

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library.add_book(book1)
library.add_book(book2)

print(library.find_book("1984").get_info())
library.list_books_by_author("Harper Lee")

book1.update_info(year=1950)
print(library.find_book("1984").get_info())

# Direct access
print(book1.author)  # Public attribute access
print(book1._title)  # Protected attribute access
# print(book1.__year)  # This would raise an AttributeError due to the private attribute
```

---

### **Explanation of Changes:**

- **Private Attribute (`__year`)**: This attribute is completely private and can only be accessed or modified through the getter and setter methods.
- **Protected Attribute (`_title`)**: This attribute is protected, meaning it is intended for internal use within the class and its subclasses but can still be accessed directly if needed.
- **Public Attribute (`author`)**: This attribute is fully public, meaning it can be accessed and modified directly.

This setup gives you a blend of access levels, allowing you to practice using private, protected, and public attributes in a realistic scenario.

---

### **Question 2: File I/O - Employee Records Processor**

#### **Objective:**
Develop a system to process employee records from a text file, perform operations on the data, and output the results to another file.

#### **Requirements:**

1. **File Processing:**
   - Write a function `process_employee_records(input_file, output_file)` that reads a text file `employees.txt` containing employee records. Each line in the file follows the format: `EmployeeID, Name, Department, Salary`.
   - Implement the following operations:
     - Calculate the average salary across all employees.
     - Identify the highest-paid employee.
     - Count the number of employees in each department.
   - Write the results to `summary.txt` in the following format:
     ```
     Average Salary: [calculated average]
     Highest Paid: [name of highest-paid employee]
     Employees per Department:
     - [Department]: [Number of Employees]
     ```

2. **Example Input (`employees.txt`):**
   ```
   001, John Doe, Engineering, 75000
   002, Jane Smith, Marketing, 65000
   003, Emily Davis, Sales, 55000
   004, Michael Brown, Engineering, 80000
   ```

3. **Example Output (`summary.txt`):**
   ```
   Average Salary: 68750.0
   Highest Paid: Michael Brown
   Employees per Department:
   - Engineering: 2
   - Marketing: 1
   - Sales: 1
   ```

---

### **Question 3: Container Manipulation - Student Grades Analysis**

#### **Objective:**
You are provided with a list of student grades and need to perform various analyses on this data using Python’s built-in data structures.

#### **Requirements:**

1. **Data Analysis:**
   - Write a function `analyze_grades(grades)` where `grades` is a list of tuples, each containing a student's name and their grade (e.g., `[("Alice", 85), ("Bob", 90), ("Charlie", 78)]`).
   - The function should:
     - Calculate the average grade.
     - Find the student with the highest grade.
     - Return a dictionary with grades as keys and lists of student names as values.

2. **Example Usage:**
   ```python
   grades = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 90)]
   result = analyze_grades(grades)
   
   print(result['average'])  # Output: 85.75
   print(result['highest'])  # Output: ['Bob', 'Diana']
   print(result['grade_distribution'])  # Output: {85: ['Alice'], 90: ['Bob', 'Diana'], 78: ['Charlie']}
   ```

---

### **Summary:**

- **Question 1 (OOP):** Manage a collection of books in a library, focusing on class design, property enforcement, and collection management.
- **Question 2 (File I/O):** Process employee records from a text file, calculate relevant statistics, and output the results to a summary file.
- **Question 3 (Container Manipulation):** Analyze student grades using lists, tuples, and dictionaries, performing operations such as averaging, finding the highest grade, and creating a grade distribution.
