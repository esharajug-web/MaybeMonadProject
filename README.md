# Maybe Monad - E-commerce Product Search System

## Project Overview

This project demonstrates the Maybe Monad using a simple e-commerce product search system implemented in Python.

The system allows users to search for products, view their original prices, calculate discounts, and display final prices.

The Maybe Monad is used to handle missing product values safely and avoid errors when a product cannot be found.

## Features

- Product search using Product ID
- Discount calculation
- Handling missing products
- Traditional implementation
- Maybe Monad implementation
- map() operation
- flat_map() operation
- get_or_else() operation
- Chained operations
- Automated testing

## Technologies Used

- Python
- Git
- Visual Studio Code

## Project Structure

CSC370-Maybe-Monad-Project/

├── main.py

├── maybe.py

├── products.py

├── test_project.py

├── README.md

└── .gitignore

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the program:

   python main.py

4. Enter a Product ID when prompted.

## How to Run Tests

Run the following command in the terminal:

   python test_project.py

The tests verify product prices, missing products, and Maybe Monad operations.

## Example Products

| Product ID | Product | Original Price | Discount | Final Price |
|------------|---------|----------------|----------|-------------|
| 101 | Laptop | $1500 | 25% | $1125 |
| 102 | Headphones | $200 | 15% | $170 |
| 103 | Keyboard | $70 | 5% | $66.50 |
| 104 | Mouse | $45 | 0% | $45 |
| 105 | Monitor | $300 | 30% | $210 |

## What is the Maybe Monad?

The Maybe Monad represents a value that may or may not exist.

In this project, it helps handle missing products safely. If a product is not found, the system returns an empty Maybe value instead of causing an error.

The Maybe class implements:

- map()
- flat_map()
- get_or_else()
