import math 

def main():
    calculator()

def calculator():
    
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
                if output == 0:
                    output = 1 * nums[i]
                else:
                    output = output * nums[i]
            elif operations[a] == "/":
                if output == 0:
                    output =  nums[i] / 1
                else:
                    output = output / nums[i]
        
    
    print("The Answer is", output)
    ready("Do you wish to continue? ", ready)
                  
if __name__ == "__main__":
    main()


