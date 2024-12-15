def function_with_uncommon_error_solution(a, b):
    if a == 0:
        #Handle the case where a is zero, e.g., raise an exception or return a default value
        raise ZeroDivisionError("Division by zero") 
        #Alternatively, return a default value like NaN or None
        #return float('nan')
        #return None
    return b / a

# Example demonstrating the corrected function
try:
    result = function_with_uncommon_error_solution(0, 10)
    print(result) 
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    result2 = function_with_uncommon_error_solution(10, 2)
    print(result2) #Output: 0.2
except ZeroDivisionError as e:
    print(f"Error: {e}") 