import os
from functools import wraps

def inject_env_vars(*env_vars):
    """
    Decorator to inject environment variables into the function's global scope.
    :param env_vars: A list of environment variable names to load.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Load environment variables into the global scope
            for var in env_vars:
                value = os.getenv(var)
                if value is None:
                    raise ValueError(f"Environment variable {var} is not set.")
                globals()[var] = value  # Inject into global scope
            
            # Call the decorated function
            return func(*args, **kwargs)
        return wrapper
    return decorator

@inject_env_vars('VARIABLE_A', 'VARIABLE_B')
def my_function():
    # Use the variables loaded by the decorator
    print(f"VARIABLE_A: {VARIABLE_A}")
    another_variable = int(VARIABLE_A) + int(VARIABLE_B)
    print(f"Sum of VARIABLE_A and VARIABLE_B: {another_variable}")
    print(f"Formatted string: bla bla bla {VARIABLE_A}")

if __name__ == "__main__":
    try:
        my_function()
    except ValueError as e:
        print(f"Error: {e}")

