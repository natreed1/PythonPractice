import math
import re 


## Try as a tree? remove nodes after using them

def get_input():
    
    ready = "False"
    nums = []
    operations = []
    operation_input = ""

    output = 0 

    while operation_input != "=":
        
        want_parens = input("Do you want to add parentheses? (y/n) ")
        if want_parens == "y":
            if "(" not in nums:
                parens = input("Enter a parenthesis: ( or ) ")
                nums.append(parens) 
            elif ")" not in nums:
                num_input = int(input("Enter an integer: "))
                parens = input("Enter a parenthesis: ( or ) ")
                operation_input = str(input("Enter an Operation: +, -, /, *, =, ^  "))
                nums.append(num_input)
                nums.append(parens)
                operations.append(operation_input)
                continue

        num_input = int(input("Enter an integer: "))
        operation_input = str(input("Enter an Operation: +, -, /, *, =, ^ "))

        if operation_input == "=":
            nums.append(num_input)
            break
        
        operations.append(operation_input)
        nums.append(num_input)
    return operations, nums
        

class Node:
    def _init__(self, value):
        self.value = value
        self.next = None

    ##using seperate lists only works for simple operations, now i need a tree to handle parantheses and order of operations.

def computation(operations, nums):
    output = 0
    if "(" in nums:
        a = nums.index("(")
        x = a - 1
        paren_index = nums.index("(")
        close_bracket_index = nums.index(")")
        while nums[a + 1] != ")":
            if operations[x] == "+":
                output += nums[a + 1] 
                nums.pop(a + 1)
                operations.pop(a)
            elif operations[x] == "-":
                output -= nums[a + 1]
                nums.pop(a + 1)
                operations.pop(a)
            elif operations[x] == "*":
                output = output * nums[a + 1]
                nums.pop(a + 1)
                operations.pop(a)
            elif operations[x] == "/":
                if nums[a + 1] == 0:
                    return "Error: Division by zero is not allowed."
            elif operations[x] == "/":
                output = output / nums[a + 1]
                nums.pop(a + 1)
                operations.pop(a)
            elif operations[x] == "^":
                output = output ** nums[a + 1]
                nums.pop(a + 1)
                operations.pop(a)
        paren_index = nums.index("(")
        nums.pop(paren_index)
        close_bracket_index = nums.index(")")
        nums.pop(close_bracket_index)    
    while nums != []:
            a = i - 1
            if operations[a] == "+":
                output += nums[i] 
                nums.pop(i)
                operations.pop(a)
            elif operations[a] == "-":
                output -= nums[i]
                nums.pop(i)
                operations.pop(a)
            elif operations[a] == "*":
                output = output * nums[i]
                nums.pop(i)
                operations.pop(a)
            elif operations[a] == "/":
                if nums[i] == 0:
                    nums.pop(i)
                    operations.pop(a)
                    return "Error: Division by zero is not allowed."
                else:
                    output = output / nums[i]
                    nums.pop(i)
                    operations.pop(a)
            elif operations[a] == "^":
                output = output ** nums[i]
    return output
        
    
def answer(output):    
    print("The Answer is", output)
    ready = input("Do you wish to continue? Yes or No: ", )
    if ready == "Yes":
        main()
    return ready

def main():
    operations, nums = get_input()
    output = computation(operations, nums)
    answer(output)


if __name__ == "__main__":
    main()


