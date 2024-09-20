import logging


def log_to_file(log_file, log_level=logging.INFO):
    #
    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    def decorator (func):
        def wrapper(*args, **kwargs):
            logging.log(log_level, f"Starting{func.__name__}")
            result = func(*args, **kwargs)  # call the original function
            logging.log(log_level,f"Finished {func.__name__}.")
            return result

        return wrapper
    return decorator

@log_to_file(log_file='custom_log.log', log_leve=logginlg.DEBUG)
def greet(name):
    print(f"Hello, {name}!")
#calling the decorated function
greet("kmnnjjk")
