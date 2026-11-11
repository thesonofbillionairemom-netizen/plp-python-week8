# Personal Mini-Toolkit

A Python-based command-line productivity application developed as part of the **Power Learn Project (PLP) – Future Proof with Python, Week 8 Final Project**.

## Project Overview

Personal Mini-Toolkit is an interactive Python application that combines three useful tools into one menu-driven program. It demonstrates fundamental Python programming concepts, including functions, loops, conditional statements, lists, exception handling, user input, and random number generation.

The project demonstrates practical problem-solving skills and the ability to develop interactive command-line applications.

## Features

### 1. Smart Calculator
- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero protection
- Input validation

### 2. Personal To-Do Manager
- Add new tasks
- View all saved tasks
- Remove tasks using their numbers
- Display the total number of tasks
- Handle invalid selections

### 3. Number Guessing Challenge
- Generates a random number between 1 and 20
- Provides higher and lower hints
- Validates user input
- Counts valid guessing attempts
- Displays a congratulatory message when the correct number is found

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## Python Concepts Demonstrated

- Variables and data types
- Functions
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while` and `for`)
- Lists and list manipulation
- User input and output
- Exception handling (`try` and `except`)
- F-strings
- Random number generation
- Built-in functions such as `len()` and `enumerate()`

## Project Structure

```text
plp-python-week8/
│
├── toolkit.py
├── toolkit_plan.txt
├── README.md
│
└── screenshots/
    ├── menu_and_invalid_choice.png
    ├── calculator_operations.png
    ├── calculator_error_handling.png
    ├── todo_manager.png
    ├── todo_manager_invalid_task.png
    └── guessing_game.png
```

## Installation and Execution

### Prerequisites

- Python 3 installed on your computer.
- A terminal or command prompt.

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/thesonofbillionairemom-netizen/plp-python-week8.git
```

**2. Navigate into the project directory**

```bash
cd plp-python-week8
```

**3. Run the application**

```bash
python toolkit.py
```

For Windows users, if the `python` command is unavailable, use:

```powershell
py toolkit.py
```

**4. Select an option from the main menu** to access any of the three tools.

## Screenshots

The `screenshots` directory contains evidence of the application's functionality, including:

- Main menu and invalid menu selection.
- Calculator operations and error handling.
- Adding, viewing, and removing tasks.
- Invalid task-number handling.
- Number guessing challenge.

## Learning Reflection

Developing this project helped me understand how different Python programming concepts work together in a practical application. The most challenging part was integrating the three tools into one menu-driven program while ensuring that each tool returned control to the main menu correctly. I also learned how to handle invalid user input using exception handling and conditional statements. One setup challenge was that the `python` command was not recognized in my Windows terminal, so I used `py toolkit.py` to execute the program. Testing each feature helped me identify input-handling issues and improve the reliability of the application. If I had another week, I would add data persistence so that tasks remain saved even after the application is closed, alongside more advanced productivity features.

## Author

**GitHub:** [thesonofbillionairemom-netizen](https://github.com/thesonofbillionairemom-netizen)

**Project:** Personal Mini-Toolkit

**Programme:** Power Learn Project – Future Proof with Python

**Assignment:** Week 8 Final Project

---

*Built with Python, curiosity, and a commitment to continuous learning.*