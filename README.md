# Arithmetic Formatter
The Arithmetic Formatter is a Python function that takes a list of arithmetic problems and arranges them vertically and side-by-side (like we used to do in elementary school). It can optionally display the answers to the problems.

Error Handling
The Arithmetic Formatter includes some error handling. 
If any of the following conditions are met, an error message will be returned:

- If there are more than 5 problems in the list, the function will return: "Error: Too many problems."
- If any of the operands contains non-digit characters, the function will return: "Error: Numbers must only contain digits."
- If the operator is not "+" or "-", the function will return: "Error: Operator must be '+' or '-'."

Example of Output

![2023-07-02](https://github.com/emanueleiacca/Arithmetic-Formatter/assets/128679981/9e109ab5-ef8d-4a46-a345-9d6f50769cb0)

# Time Calculator

The Time Calculator is a Python function that adds a duration to a given start time and returns the resulting time. It can also handle optional parameters such as the starting day of the week. The function supports both 12-hour and 24-hour clock formats.

Dependencies

The Time Calculator function does not rely on any external Python libraries

Usage Examples

![2023-07-02 (2)](https://github.com/emanueleiacca/Time-calculator/assets/128679981/57c92b42-5cf1-4481-a12e-9a39e8f6fe5b)


![2023-07-02 (2)1](https://github.com/emanueleiacca/Time-calculator/assets/128679981/6886f41e-1d5f-4ae5-a80b-e860f9c66346)

# Budget-App

The Budget Management System is a Python project that allows you to track and manage your expenses across different categories. It provides a Category class for creating expense categories and includes a charting feature to visualize the percentage spent by category.

## Features

- Create and manage expense categories
- Perform deposits, withdrawals, and transfers between categories
- Calculate and display the balance for each category
- Generate a spend chart to visualize the percentage spent by category

##Examples of Usage

![2023-07-02 (4)](https://github.com/emanueleiacca/Budget-App/assets/128679981/43b705b3-9c78-4285-a2a3-3ee175a5bd13)

![2023-07-02 (3)](https://github.com/emanueleiacca/Budget-App/assets/128679981/de5dff8d-1a91-4be2-a616-49c1a6208a04)

# Polygon-Area-Calculator
This project is a Polygon Area Calculator implemented in Python. It includes two classes: Rectangle and Square, which demonstrate object-oriented programming concepts and inheritance.

##Rectangle class
The Rectangle class represents a rectangle shape. It has the following attributes and methods:

Attributes

width: The width of the rectangle.

height: The height of the rectangle.

Methods

__init__(self, width, height): The constructor method that initializes the width and height of the rectangle.

set_width(self, width): Sets the width of the rectangle.

set_height(self, height): Sets the height of the rectangle.

get_area(self): Calculates and returns the area of the rectangle.

get_perimeter(self): Calculates and returns the perimeter of the rectangle.

get_diagonal(self): Calculates and returns the diagonal of the rectangle.

get_picture(self): Returns a string representation of the rectangle using "*" to depict the shape. If the dimensions exceed 50, it returns "Too big for picture."

get_amount_inside(self, shape): Returns the number of times a given shape can fit inside the rectangle.

__str__(self): Provides a string representation of the rectangle object.

##Square class

The Square class is a subclass of the Rectangle class. It inherits the attributes and methods of the Rectangle class but adds additional functionality specific to squares.

Methods

__init__(self, side): The constructor method that initializes the side length of the square. It calls the constructor of the Rectangle class.

set_side(self, side): Sets the side length of the square.

__str__(self): Provides a string representation of the square object.

##Examples Usages

![2023-07-02 (6)1](https://github.com/emanueleiacca/Polygon-Area-Calculator/assets/128679981/ecd73cbe-8a06-4b32-aa46-96cd6c6edd97)

![2023-07-02 (5)](https://github.com/emanueleiacca/Polygon-Area-Calculator/assets/128679981/67207473-347a-4b6f-a5e5-384d35e9dd64)

# Probability-calculator
This project is a probability calculator that estimates the likelihood of drawing specific balls from a hat. It uses Python programming language to simulate drawing experiments and calculate probabilities based on the results.

Project Overview
The probability calculator consists of the following components:

prob_calculator.py: This file contains the implementation of the Hat class and the experiment function. The Hat class represents a collection of colored balls, and the experiment function calculates the probability of drawing a specific group of balls from the hat.

main.py: This file is provided for testing the code and running experiments. It imports the necessary modules and executes the code in prob_calculator.py.

test_module.py: This file contains unit tests to verify the correctness of the code implementation. It checks the behavior of the Hat class and the experiment function.

Explanation of results:

each time we run the code we will obtain a different results, because the number of experiment is too low (1000), therefore the obtained result is not empirical
