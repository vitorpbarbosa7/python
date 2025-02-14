import os
from functools import wraps

# Decorator definition
def apply_env_vars(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Add global environment variables
        os.environ["GLOBAL_VAR_A"] = "ValueA"
        os.environ["GLOBAL_VAR_B"] = "ValueB"
        # or use getenv
        
        print(f"Environment variables set: {os.environ['GLOBAL_VAR_A']}, {os.environ['GLOBAL_VAR_B']}")
        
        # Helper function to wrap any internal function calls
        def decorate_internal_calls(inner_func):
            @wraps(inner_func)
            def internal_wrapper(*args, **kwargs):
                print(f"Internal function `{inner_func.__name__}` is being decorated.")
                result = inner_func(*args, **kwargs)
                return result
            return internal_wrapper
        
        # Apply the decorator to all internal functions called
        def wrapped_function():
            # Manually patch internal functions
            globals()["other_funca"] = decorate_internal_calls(globals()["other_funca"])
            globals()["other_funcb"] = decorate_internal_calls(globals()["other_funcb"])
            return func(*args, **kwargs)
        
        return wrapped_function()

    return wrapper

# Example internal functions
def other_funca():
    print("Executing `other_funca`.")
    return "Result from other_funca"

def other_funcb():
    print("Executing `other_funcb`.")
    return "Result from other_funcb"

# Main function with the decorator
@apply_env_vars
def mother_fun():
    print("Executing `mother_fun`.")
    results_a = other_funca()
    results_b = other_funcb()
    print(f"Results: {results_a}, {results_b}")

# Run the main function
mother_fun()

