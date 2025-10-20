# Calculator.py
# Simple CLI Calculator

A minimal command-line calculator written in Python. Supports addition, subtraction, multiplication and division via an interactive prompt.

## Features
- Add, subtract, multiply, divide
- Input validation for numbers
- Graceful handling of division by zero and keyboard interrupt

## Usage
Requirements: Python 3.6+

Follow the on-screen menu to choose an operation or quit.

## Files
- Calculator.py — main CLI application

  
##How it works 

- Docstring: describes the script and how to run it.

- import sys: allows clean exit on Ctrl+C.

- Operations: add, subtract, multiply, divide (divide raises on zero).

- get_number(prompt): keeps asking until a valid float is entered.

main():
 - Builds a menu and maps choices ("1"–"4") to (symbol, function).

 - Loops: shows menu, reads choice; quits on q/quit/exit; rejects invalid choices.

 - For a valid choice: prompts for two numbers, calls the operation inside try/except to handle division-by-zero.

 - Formats result to drop trailing .0 for integer values and prints "a symbol b = result".

 - if name == "main": runs main() and handles KeyboardInterrupt to exit cleanly.
