def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    #checking if the number of problem in the list exceeds 5
    
    top_line = []
    bottom_line = []
    divider_line = []
    result_line = []
    #empty list to store the arranged problems
    for problem in problems:
        operand1, operator, operand2 = problem.split()
        #in loop to split the problem into 3 parts
        if not operand1.isdigit() or not operand2.isdigit():
            #check that each parts contain only digits
            return "Error: Numbers must only contain digits."
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        #check that the operaton is only plus or minus
        
        width = max(len(operand1), len(operand2)) + 2  
        # max Width of each line for spacing
        
        top_line.append(operand1.rjust(width))
        bottom_line.append(operator + operand2.rjust(width - 1))
        divider_line.append('-' * width)
        #i made the line equal to the max width, like we used to do in elementary school
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            result_line.append(result.rjust(width))
            #explaining to code what to do for both the operation
    
    arranged_problems = []
    arranged_problems.append('    '.join(top_line))
    arranged_problems.append('    '.join(bottom_line))
    arranged_problems.append('    '.join(divider_line))
    #add space between each problem to help the readers
    
    if show_answers:
        arranged_problems.append('    '.join(result_line))
    
    return '\n'.join(arranged_problems)
#example below to see if the code works correctly

problems_with_answers = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems_with_answers, True))

