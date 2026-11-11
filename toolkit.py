
import random


# =============================================
# TOOL 1: SMART CALCULATOR
# =============================================

def smart_calculator():

    while True:
        print("\n=============================================")
        print("             SMART CALCULATOR")
        print("=============================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Return to Main Menu")
        print("=============================================")

        choice = input("Select an operation (1-5): ")

        if choice == "5":
            print("Returning to Main Menu...")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select 1-5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = num1 + num2
                print(f"Result: {num1:g} + {num2:g} = {result:g}")

            elif choice == "2":
                result = num1 - num2
                print(f"Result: {num1:g} - {num2:g} = {result:g}")

            elif choice == "3":
                result = num1 * num2
                print(f"Result: {num1:g} * {num2:g} = {result:g}")

            elif choice == "4":
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1:g} / {num2:g} = {result:g}")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")


# =============================================
# TOOL 2: PERSONAL TO-DO MANAGER
# =============================================

def todo_manager():

    tasks = []

    while True:
        print("\n=============================================")
        print("          PERSONAL TO-DO MANAGER")
        print("=============================================")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Return to Main Menu")
        print("=============================================")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            task = input("Enter your new task: ").strip()

            if task:
                tasks.append(task)
                print(f"Success! '{task}' has been added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your task list is currently empty.")
            else:
                print("\nYOUR TASK LIST")
                print("---------------------------------------------")

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                print("---------------------------------------------")
                print(f"Total tasks: {len(tasks)}")

        elif choice == "3":
            if not tasks:
                print("No tasks available to remove.")
            else:
                print("\nYOUR TASK LIST")

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Success! '{removed_task}' has been removed.")
                    else:
                        print("Invalid task number. Please try again.")

                except ValueError:
                    print("Invalid input! Please enter a whole number.")

        elif choice == "4":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please select 1-4.")


# =============================================
# TOOL 3: NUMBER GUESSING CHALLENGE
# =============================================

def number_guessing_game():

    secret_number = random.randint(1, 20)
    attempts = 0

    print("\n=============================================")
    print("          NUMBER GUESSING CHALLENGE")
    print("=============================================")
    print("I have selected a secret number between 1 and 20.")
    print("Can you guess it?")
    print("=============================================")

    while True:

        try:
            guess = int(input("Enter your guess (1-20): "))

            if guess < 1 or guess > 20:
                print("Out of range! Enter a number between 1 and 20.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")

            elif guess > secret_number:
                print("Too high! Try a lower number.")

            else:
                print("\nCongratulations! You guessed the correct number.")
                print(f"The secret number was {secret_number}.")
                print(f"Number of attempts: {attempts}")
                print("Great job!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# =============================================
# MAIN APPLICATION
# =============================================

print("\n=============================================")
print("          PERSONAL MINI-TOOLKIT")
print("=============================================")
print("Welcome! Your productivity toolkit is ready.")
print("Explore the tools and enjoy using Python!")

while True:

    print("\n=============================================")
    print("                 MAIN MENU")
    print("=============================================")
    print("1. Smart Calculator")
    print("2. Personal To-Do Manager")
    print("3. Number Guessing Challenge")
    print("4. Quit")
    print("=============================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        smart_calculator()

    elif choice == "2":
        todo_manager()

    elif choice == "3":
        number_guessing_game()

    elif choice == "4":
        print("\nThank you for using Personal Mini-Toolkit!")
        print("Goodbye! Keep learning and stay productive.")
        break

    else:
        print("Invalid choice! Please select a number from 1 to 4.")
