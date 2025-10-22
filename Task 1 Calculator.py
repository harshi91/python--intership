import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def main():
    menu = (
        "\nCalculator - choose an operation:\n"
        "1) Add (+)\n"
        "2) Subtract (-)\n"
        "3) Multiply (*)\n"
        "4) Divide (/)\n"
        "q) Quit\n"
    )
    ops = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    while True:
        print(menu)
        choice = input("Enter choice: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye.")
            break
        if choice not in ops:
            print("Invalid choice. Select 1-4 or q to quit.")
            continue

        symbol, func = ops[choice]
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        try:
            result = func(a, b)
        except ZeroDivisionError as e:
            print("Error:", e)
            continue

        # Print integer-looking results without trailing .0
        if result.is_integer():
            result_display = int(result)
        else:
            result_display = result
        print(f"{a} {symbol} {b} = {result_display}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

        sys.exit(0)

