import math 

def main():
    
    ready = "False"
    nums = []
    operations = []

    output = 0 
    count = 0

    while ready == "F" or ready == "False":
        operation_input = str(input("Enter an Operation: +, -, /, * "))
        operations.append(operation_input)
        
        num_input = int(input("Enter an integer: "))
        ready = input("Are You Finished? Enter T or F ")    
        nums.append(num_input)
        count += 1
    
    while ready == "T" or "True":
        for i in range(len(operations)):
            if operations[i] == "+":
                output += nums[i] 
            elif operations[i] == "-":
                output -= nums[i]
            elif operations[i] == "*":
                output = output * nums[i]
            elif operations[i] == "/":
                output = output / nums[i]
        break
    
    print("The Answer is ", output)
    ready("Do you wish to continue? ", ready)
                  
main()



