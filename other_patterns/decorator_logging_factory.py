import logging

'''
This script demonstrates a decorator factory that allows you to specify the logging level for logging function calls and their return values.
The decorator can be applied to any function, and it will log the function's name, arguments, keyword arguments, and return value at the specified 
logging level.
'''
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Decorator factory to accept logging level
def log_decorator(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            log_message = f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}"
            # Log based on the specified level
            if level == 'debug':
                logging.debug(log_message)
            elif level == 'info':
                logging.info(log_message)
            elif level == 'warning':
                logging.warning(log_message)
            elif level == 'error':
                logging.error(log_message)
            elif level == 'critical':
                logging.critical(log_message)
            
            # Execute the original function
            result = func(*args, **kwargs)

            # Log the function's return value
            if level == 'debug':
                logging.debug(f"Function '{func.__name__}' returned: {result}")
            elif level == 'info':
                logging.info(f"Function '{func.__name__}' returned: {result}")
            elif level == 'warning':
                logging.warning(f"Function '{func.__name__}' returned: {result}")
            elif level == 'error':
                logging.error(f"Function '{func.__name__}' returned: {result}")
            elif level == 'critical':
                logging.critical(f"Function '{func.__name__}' returned: {result}")
            
            return result
        return wrapper
    return decorator

# Applying the decorator with a specified logging level
@log_decorator(level='info')
def add(a, b):
    return a + b

@log_decorator(level='info')
def greet(name):
    return f"Hello, {name}!"

# Using the functions
add(10, 20)
greet(name="Hooman")