def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # This is not an error, but a common mistake in this type of function
    return b / a

# Example of the uncommon error: the function may raise ZeroDivisionError if a is 0, but not in all cases
result = function_with_uncommon_error(0, 10)
print(result) # Output: 0

# Example that will trigger ZeroDivisionError 
result2 = function_with_uncommon_error(0,1)
print(result2)