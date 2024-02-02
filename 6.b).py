class FormulaError(Exception):
    pass

def calculate(formula):
    try:
        values = formula.split()
        if len(values) != 3:
            raise FormulaError("Invalid formula. Please enter a formula with three elements separated by whitespace.")

        num1 = float(values[0])
        operator = values[1]
        num2 = float(values[2])

        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator. Please use only '+' or '-' as the operator.")

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2

        print("Result:", result)
    except ValueError:
        raise FormulaError("Invalid input. Please enter valid numbers.")
    except FormulaError as e:
        print("Error:", e)

# Main loop for the interactive calculator
while True:
    user_input = input("Enter a formula (e.g., 1 + 1), or type 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break

    try:
        calculate(user_input)
    except FormulaError as e:
        print("Error:", e)
