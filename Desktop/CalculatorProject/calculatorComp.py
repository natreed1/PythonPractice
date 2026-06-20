import math
import re 


def get_input():
    
    ready = "False"
    nums = []
    operations = []
    operation_input = ""

    output = 0 

    while operation_input != "=":

        num_input = int(input("Enter an integer: "))
        operation_input = str(input("Enter an Operation: +, -, /, *, = "))
        
        if operation_input == "=":
            nums.append(num_input)
            break
        
        operations.append(operation_input)
        nums.append(num_input)
    return operations, nums
        
def computation(operations, nums):
    output = 0
    for i in range(len(nums)): 
        if i == 0:
            output = nums[i]
        else:
            a = i - 1
            if operations[a] == "+":
                output += nums[i] 
            elif operations[a] == "-":
                output -= nums[i]
            elif operations[a] == "*":
                output = output * nums[i]
            elif operations[a] == "/":
                if nums[i] == 0:
                    return "Error: Division by zero is not allowed."
                else:
                    output = output / nums[i]
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


