import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(filename)s, Line %(lineno)d - PID:%(process)d - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# Applying the decorator
@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name):
    return f"Hello, {name}!"

# Using the functions
add(10, 20)
greet(name="Hooman")