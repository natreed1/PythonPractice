import math 

def main():
    
    ready = "False"
    nums = []
    operations = []

    output = 0 
    count = 0

    while ready == "F" or ready == "False":
        
        ##if (len(nums)) != 0:
        num_input = int(input("Enter an integer: "))
        ready = input("Are You Finished? Enter T or F ")    
        
        if ready == "T" or ready == "True":
            nums.append(num_input)
            break
        
        operation_input = str(input("Enter an Operation: +, -, /, * "))
        
        operations.append(operation_input)
        nums.append(num_input)
        count += 1
    
    
    while ready == "T" or ready == "True":
        if not operations:
            output = nums[0]
            break
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
        break
    
    print("The Answer is", output)
    ready("Do you wish to continue? ", ready)
                  
main()



