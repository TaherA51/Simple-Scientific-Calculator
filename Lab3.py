# Lab 3 - Scientific Calculator
# This program simulates a scientific calculator that can perform various operations
# including addition, subtraction, multiplication, division, exponentiation, logarithms,
# and it can also calculate the average of all results computed so far.

import math  # Importing the math module for advanced mathematical functions
import sys   # Importing the sys module to allow the program to exit

# Initialize the current result and result history list
current_result = float(0)  # Holds the current result of calculations
result_list = []  # List to store all results for calculating the average

while True:

    # Variable to store user menu selection
    menu_select = None

    # Function to display the calculator menu
    def menu():
        print(f'Current Result: {current_result} \n')
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average \n")

    # Function to check if operands are numbers or the previous result
    def check_operand(operand1, operand2):
        if operand1.upper() == 'RESULT':  # Use 'RESULT' keyword for current result
            operand1 = current_result
        else:
            operand1 = float(operand1)  # Convert operand to float if not 'RESULT'
        if operand2.upper() == 'RESULT':
            operand2 = current_result
        else:
            operand2 = float(operand2)

        return operand1, operand2

    # Function for addition
    def addition():
        global current_result
        operand1 = input('Enter first operand: ')
        operand2 = input('Enter second operand: ')
        operand1, operand2 = check_operand(operand1, operand2)
        current_result = float(operand1) + float(operand2)
        result_list.append(current_result)  # Append result to history
        return current_result, result_list

    # Function for subtraction
    def subtraction():
        global current_result
        operand1 = input('Enter first operand: ')
        operand2 = input('Enter second operand: ')
        operand1, operand2 = check_operand(operand1, operand2)
        current_result = float(operand1) - float(operand2)
        result_list.append(current_result)
        return current_result, result_list

    # Function for multiplication
    def multiplication():
        global current_result
        operand1 = input('Enter first operand: ')
        operand2 = input('Enter second operand: ')
        operand1, operand2 = check_operand(operand1, operand2)
        current_result = float(operand1) * float(operand2)
        result_list.append(current_result)
        return current_result, result_list

    # Function for division
    def division():
        global current_result
        operand1 = input('Enter first operand: ')
        operand2 = input('Enter second operand: ')
        operand1, operand2 = check_operand(operand1, operand2)
        if operand2 == 0:  # Check for division by zero
            print("Error: invalid input!")
        else:
            current_result = float(operand1) / float(operand2)
            result_list.append(current_result)
            return current_result, result_list

    # Function for exponentiation
    def exponentiation():
        global current_result
        operand1 = input('Enter first operand: ')
        operand2 = input('Enter second operand: ')
        operand1, operand2 = check_operand(operand1, operand2)
        current_result = float(operand1) ** float(operand2)  # Raise operand1 to the power of operand2
        result_list.append(current_result)
        return current_result, result_list

    # Function for logarithm calculation
    def logarithm():
        global current_result
        operand1 = input('Enter first operand: ')  # Base of the logarithm
        operand2 = input('Enter second operand: ')  # Argument of the logarithm
        operand1, operand2 = check_operand(operand1, operand2)
        if operand1 <= 0 or operand2 <= 0:  # Logarithms are undefined for non-positive numbers
            print('Error: invalid input!')
        else:
            current_result = math.log(float(operand2), float(operand1))  # Logarithm of operand2 base operand1
            result_list.append(current_result)
            return current_result, result_list

    # Function to calculate the average of all previous results
    def average():
        total = 0
        if len(result_list) == 0:
            print("Error: No calculations yet to average! \n")
        else:
            for x in range(len(result_list)):
                total += result_list[x]
            print(f'Sum of calculations: {total}')
            print(f'Number of calculations: {len(result_list)}')
            print(f'Average of calculations: {total/len(result_list):.2f} \n')

    # Show the menu to the user
    menu()

    running = True

    # Main program loop that runs based on user's menu selection
    while running:

        menu_select = int(input('Enter Menu Selection: '))  # Read user input for operation

        # Exit the program
        if menu_select == 0:
            print("Thanks for using this calculator. Goodbye!")
            sys.exit(0)

        # Perform operations based on the user's choice
        elif menu_select == 1:
            addition()
            break

        elif menu_select == 2:
            subtraction()
            break

        elif menu_select == 3:
            multiplication()
            break

        elif menu_select == 4:
            division()
            break

        elif menu_select == 5:
            exponentiation()
            break

        elif menu_select == 6:
            logarithm()
            break

        elif menu_select == 7:
            average()

        else:
            print('Error: Invalid selection! \n')
            continue
