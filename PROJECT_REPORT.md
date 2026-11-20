# Implementing the Maybe Monad in Python
## E-Commerce Product Search System

## 1. Introduction

This project demonstrates the concept of Monads using a simple e-commerce product search system developed in Python.

The system allows users to search for products using a Product ID, view the original price, check the discount, and calculate the final price.

The project focuses on the Maybe Monad, which helps handle situations where a value may be missing. For example, when searching for a product, the system may find the product or it may not exist in the database.

To understand how the Maybe Monad works, the project compares a traditional programming approach with an approach using the Maybe Monad. This helps show how Monads can make handling missing values easier and safer.

## 2. What is a Monad?

A Monad is a programming concept used to work with values that are placed inside a particular context.

Instead of working directly with a value, a Monad wraps the value and provides methods to perform operations on it.

In this project, we use the Maybe Monad. It is useful when a value may exist or may be missing.

For example, when searching for a product, the system may return the product details if the product exists. If the product does not exist, it returns a missing value.

The Maybe Monad helps us handle both situations without causing errors.

## 3. What Problem Does a Monad Solve?

In normal programming, when a function returns a missing value, we need to check whether the value exists before performing another operation.

For example, if a product is not found, trying to access its price or calculate its discount could cause an error.

The Maybe Monad helps solve this problem by safely handling missing values.

If a value exists, the operation is performed normally. If the value is missing, the operation is skipped and the missing value is passed along.

This reduces the need for repeated checks and makes the code easier to read and manage.

## 4. Language Features Required

To implement the Maybe Monad, the programming language needs certain features that allow us to store values, create functions, and handle missing data.

Python provides all the features needed for this project.

The main features used are:

- Classes and objects: These allow us to create the Maybe class and store values inside objects.
- Functions: Functions are used to search for products, calculate discounts, and perform operations on values.
- None: Python uses None to represent a missing or empty value.
- Higher-order functions: Methods such as map() and flat_map() accept other functions as arguments, allowing operations to be performed on values inside the Maybe object.
- Lambda functions: These are small functions used for simple operations, such as rounding a price.
- Dictionaries: Dictionaries are used to store product information and allow products to be searched using their Product IDs.

These features make Python suitable for implementing the Maybe Monad in this project.

## 5. Why We Chose the Maybe Monad

We chose the Maybe Monad because our product search system deals with situations where a product may or may not exist.

For example, when a user searches for Product ID 102, the system finds the headphones and calculates the final price. However, when the user searches for Product ID 999, the product does not exist.

Without the Maybe Monad, we would need to check for missing values repeatedly before performing different operations. The Maybe Monad helps handle these situations in a safer and simpler way.

It allows us to perform operations only when a value exists. If the value is missing, the operation is skipped instead of causing an error.

We chose the Maybe Monad because it is simple to implement and clearly demonstrates how Monads can be useful in real-world programming.

## 6. Project Overview

The project is a simple e-commerce product search system that allows users to search for products using their Product ID.

Each product contains its name, original price, and discount percentage. The system calculates the final price after applying the discount.

The project has two implementations:

- Traditional implementation: Uses normal functions and conditional statements to handle product searches and missing values.
- Maybe Monad implementation: Uses the Maybe class to handle values that may be missing.

The main goal is to compare these two approaches and understand how the Maybe Monad can help manage missing values.

## 7. Product Database

The project uses a Python dictionary to store product information.

Each product is identified by a unique Product ID. The database contains five products.

| Product ID | Product | Price | Discount |
|---|---|---:|---:|
| 101 | Laptop | $1500 | 25% |
| 102 | Headphones | $200 | 15% |
| 103 | Keyboard | $70 | 5% |
| 104 | Mouse | $45 | 0% |
| 105 | Monitor | $300 | 30% |

The dictionary makes it easy to search for a product using its ID and retrieve its details.

## 8. Traditional Implementation

The traditional implementation uses normal Python functions to search for products and calculate their final prices.

The `search_product()` function checks whether the Product ID exists in the database. If the product is found, its details are returned. If it is not found, the function returns `None`.

The `calculate_final_price()` function calculates the discounted price. Before performing the calculation, it checks whether the product exists.

The `display_product()` function combines these operations and displays the product information.

This approach works correctly, but it requires conditional checks to handle missing values.

## 9. Maybe Monad Implementation

The Maybe Monad is implemented using a Python class called `Maybe`.

The class stores a value inside an object. The value may be present or it may be `None`.

The Maybe class provides methods that allow us to perform operations on the stored value safely.

The methods implemented in our project are:

- `map()`
- `flat_map()`
- `get_or_else()`
- `is_present()`
- `is_empty()`

These methods help us work with values without repeatedly checking whether they exist.

## 10. The Maybe Class

The Maybe class is defined in `maybe.py`.

The constructor stores the value inside the Maybe object.

The `map()` method performs an operation on the stored value. If the value is missing, it returns an empty Maybe object instead of performing the operation.

The `flat_map()` method works similarly to `map()`, but it is used when the function itself returns another Maybe object. It avoids creating unnecessary nested Maybe objects.

The `get_or_else()` method returns the stored value if it exists. If the value is missing, it returns a default value.

The `is_present()` method checks whether a value exists.

The `is_empty()` method checks whether the value is missing.

Together, these methods allow the Maybe Monad to handle missing values safely.

## 11. Product Search Using Maybe

The function `search_product_maybe()` searches for a product using its Product ID.

Instead of returning the product directly, it wraps the result inside a Maybe object.

If the product exists, the Maybe object contains the product details.

If the product does not exist, the Maybe object contains `None`.

This allows the program to handle both situations using the same structure.

## 12. Discount Calculation

The function `calculate_discounted_price()` calculates the final price of a product after applying the discount.

The calculation is performed using the following formula:

Final Price = Original Price - (Original Price × Discount / 100)

For example, the Laptop has an original price of $1500 and a discount of 25%.

Final Price = 1500 - (1500 × 25 / 100)

Final Price = $1125

The function returns the calculated price inside a Maybe object.

## 13. Chaining Operations

One of the important features demonstrated in this project is chaining operations using the Maybe Monad.

The `get_final_price()` function performs multiple operations in sequence.

First, it searches for the product.

Next, it calculates the discounted price using `flat_map()`.

Finally, it rounds the price using `map()`.

If the product is missing, the operations are safely skipped and the system returns "Product not found".

This demonstrates how the Maybe Monad allows multiple operations to be connected without repeatedly checking for missing values.

## 14. Automated Testing

The project includes a separate testing file called `test_project.py`.

The testing file checks whether the program works correctly.

The tests include:

- Checking the final prices of all five products.
- Checking whether a missing product returns "Product not found".
- Testing the `map()` method.
- Testing the `flat_map()` method.
- Testing the `get_or_else()` method.
- Testing how the Maybe Monad handles `None`.
- Testing the `is_present()` method.
- Testing the `is_empty()` method.

The tests use Python's `assert` statements to check whether the expected results are returned.

If all tests pass, the program displays a message confirming that the tests were successful.

## 15. Language Analysis: Python

Python was used to implement the Maybe Monad because it is simple and easy to understand.

Python supports classes, functions, dictionaries, lambda functions, and higher-order functions, which were useful for implementing the Maybe Monad.

The language also provides `None`, which can be used to represent a missing value.

The use of Python made the implementation easier to develop, test, and understand.

### Helpful Features

The following Python features were helpful in this project:

- Classes allowed us to create the Maybe class.
- Functions allowed us to separate different operations.
- Dictionaries allowed us to store and search product information.
- Lambda functions allowed us to perform simple operations while chaining.
- `None` helped represent missing values.
- Higher-order functions allowed methods such as `map()` and `flat_map()` to accept other functions as arguments.

### Difficulties

One of the main difficulties was understanding how the Maybe Monad works and how it differs from normal programming.

Another challenge was understanding the difference between `map()` and `flat_map()`.

We also had to make sure that operations were not performed when the value was missing.

Testing different situations, such as searching for an existing product and a missing product, helped us understand how the Maybe Monad works.

## 16. Connection to Course Concepts

### Type System

The Maybe class creates a structure that can hold either a value or a missing value.

This demonstrates how values can be represented using different types or structures.

### Data Abstraction

The Maybe class hides the details of how missing values are handled.

Instead of directly checking the value every time, the user can call methods such as `map()`, `flat_map()`, and `get_or_else()`.

### Procedural Abstraction

The project separates different operations into functions.

For example, searching for a product, calculating a discount, and displaying the result are handled by separate functions.

This makes the program easier to understand and maintain.

### Functional Programming

The project demonstrates functional programming concepts through the use of `map()`, `flat_map()`, and lambda functions.

These methods allow operations to be performed on values without directly modifying the Maybe object.

### Object-Oriented Programming

The Maybe Monad is implemented using a Python class.

The class contains data and methods that operate on that data.

This demonstrates the use of objects and methods in Python.

## 17. Traditional Implementation vs. Maybe Monad

The traditional implementation uses conditional statements to check whether a product exists before performing operations.

The Maybe Monad provides methods to handle missing values in a more organized way.

| Traditional Implementation | Maybe Monad Implementation |
|---|---|
| Uses conditional checks | Uses Maybe methods |
| Returns `None` when a product is missing | Wraps the result inside a Maybe object |
| Requires checks before operations | Operations are safely skipped when the value is missing |
| Uses normal functions | Uses methods such as `map()` and `flat_map()` |
| Can become repetitive when handling missing values | Makes chained operations easier to manage |

Both implementations work correctly in this project.

The traditional approach is simple and easy to understand. However, the Maybe Monad provides a more organized way to handle missing values, especially when multiple operations need to be performed.

## 18. Results

The project was successfully implemented and tested using Python.

The system correctly searches for products, calculates discounts, and displays the final prices.

The Maybe Monad successfully handles missing products without causing errors.

The automated tests confirmed that the product calculations and Maybe Monad methods work as expected.

The project also demonstrates the difference between traditional programming and using a Monad to handle missing values.

## 19. Conclusion

This project helped us understand the concept of Monads and how they can be used in programming.

By implementing the Maybe Monad in Python, we learned how to handle values that may be missing.

The project also helped us understand methods such as `map()`, `flat_map()`, and `get_or_else()`.

Comparing the traditional implementation with the Maybe Monad showed us how Monads can make certain operations easier to manage and reduce repeated checks for missing values.

Overall, the project provided a practical way to understand Monads and their use in programming.

## 20. References

1. Gabbrielli, M., & Martini, S. (2023). *Programming Languages: Principles and Paradigms* (2nd ed.). Springer Nature Switzerland AG.

2. Wadler, P. (1995). Monads for functional programming. In J. Jeuring & E. Meijer (Eds.), *Advanced Functional Programming* (pp. 24–52). Springer.

3. Python Software Foundation. *Python Documentation*. https://docs.python.org/3/
