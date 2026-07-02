import re
import math
from typing import Union
    

def process_input(expressionInput: str, variable_name, variable_value) -> list[str]:
    expression = expressionInput.lower().split() 
    if variable_name == "":
        return expression
    expression = insert_variable(expression, variable_name, variable_value)
    return expression 

def process_variable(variable: str) -> tuple[str, float]:
    parts = variable.split("=")
    variable_name = parts[0].strip().lower()
    variable_expression = parts[1].strip().lower()
    variable_value = computation(variable_expression.split())
    return variable_name, variable_value


def add_variable() -> list[str]:
    variable = input("Please enter a variable and its value (ex: x = 5): ")
    return process_variable(variable)

     
def process_parentheses(expression: list[str]) -> list[str]:
    if "(" in expression:
        start = expression.index("(")
        end = expression.index(")")
        sub_expression = expression[start + 1:end]
        result = computation(sub_expression)
        expression[start:end + 1] = [str(result)]
    return expression

def insert_variable(expression: list[str], variable_name: str, variable_value: float) -> list[str]: 
    for i in range(len(expression)):
        if expression[i] == variable_name:
            expression[i] = str(variable_value)
    return expression

def computation(expression) -> float:
    output = 0 
    current = 0 

    if len(expression) == 1:
        return float(expression[0])
    
    while current + 1 < len(expression):
        if expression[current + 1] == "+":
            left_num = float(expression[current])
            right_num = float(expression[current + 2])
            output = left_num + right_num
            expression[current: current + 3] = [str(output)]
        elif expression[current + 1] == "*":
            left_num = float(expression[current])
            right_num = float(expression[current + 2])
            output = left_num * right_num
            expression[current: current + 3] = [str(output)]
        elif expression[current + 1] == "-":
            left_num = float(expression[current])
            right_num = float(expression[current + 2])
            output = left_num - right_num
            expression[current: current + 3] = [str(output)]
        elif expression[current + 1] == "/":
            left_num = float(expression[current])
            right_num = float(expression[current + 2])
            if right_num == 0:
                print("Error: Division by zero is not allowed.")
                return None
            else:
                output = left_num / right_num
                expression[current: current + 3] = [str(output)]
    return output 

def answer(output) -> None:
    print("The answer is ", output)


def calculate(expressionInput: list, variable_name: str, variable_value: float) -> Union[float, int]:
    expression = process_input(expressionInput, variable_name, variable_value)
    expression = process_parentheses(expression)
    output = computation(expression)
    if isinstance(output, float):
        if output.is_integer():
            return int(output)
    return output

def main() -> None:
    print("Welcome to the calculator! Input 'exit' to complete")
    while True:
        add_variable_choice = input("Would you like to add a variable? (y/n): ")
        if add_variable_choice.lower().strip() == "y":
            variable_name, variable_value = add_variable()
        expr = input("> ")
        if expr.lower().strip() == "exit": 
            return
        if add_variable_choice.lower().strip() != "y":
            variable_name = ""
            variable_value = 0.0
            result = calculate(expr, variable_name, variable_value)
        else:
            result = calculate(expr, variable_name, variable_value)
        print(result) 

if __name__ == "__main__":
    main()
