import logging
import sys
from io import StringIO

'''
Decorator to log function calls, including arguments, printed output, and return values.
This decorator captures the output of print statements within the function and logs them at the specified logging level.
'''

# Configure logging
logging.basicConfig(
    # format='%(asctime)s - %(levelname)s - %(filename)s, Line %(lineno)d - PID:%(process)d - %(message)s', 
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def log_decorator_with_prints(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Redirect `print` output
            original_stdout = sys.stdout
            sys.stdout = StringIO()  # Temporary buffer to capture printed messages
            log_message = f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}"
            
            # Log the function call based on the level
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
            
            try:
                # Execute the original function and capture the result
                result = func(*args, **kwargs)
                
                # Capture any printed output
                printed_output = sys.stdout.getvalue()
                if printed_output:  # Log captured prints
                    log_message = f"Printed output from '{func.__name__}': {printed_output.strip()}"
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
                
                # Log the return value of the function
                log_message = f"Function '{func.__name__}' returned: {result}"
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
                
                return result
            finally:
                # Restore the original stdout
                sys.stdout = original_stdout
        return wrapper
    return decorator

# Applying the decorator
@log_decorator_with_prints(level='info')
def demo_function(x, y):
    print(f"Adding numbers: {x} + {y}")
    return x + y

# Using the function
demo_function(5, 7)