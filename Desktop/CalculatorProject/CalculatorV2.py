import re
import math

def get_input() -> str:
    print("Welcome to the calculator!")
    print("Please split up each individual number and operator with a space.")
    example = input("Would you like to see an example? (y/n) " )
    if example == "y":
        print("Example: 2 + ( 3 * 4 )")
        print("This would evaluate to 14.") 
    expressionInput = input("Enter a mathematical expression: ")
    return expressionInput

    

def process_input(expressionInput: str) -> list[str]:
    expression =  expressionInput.split()
    return expression 

def process_parentheses(expression: list[str]) -> list[str]:
    if "(" in expression:
        start = expression.index("(")
        end = expression.index(")")
        sub_expression = expression[start + 1:end]
        result = computation(sub_expression)
        expression[start:end + 1] = [str(result)]
    return expression


def computation(expression) -> float:
    output = 0 
    current = 0 

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


def calculate(expressionInput: list) -> float:
    expression = process_input(expressionInput)
    expression = process_parentheses(expression)
    output = computation(expression)
    return output

def main() -> None:
    expressionInput = get_input()
    output = calculate(expressionInput)
    answer(output)

if __name__ == "__main__":
    main()
