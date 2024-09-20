import time
def log_func_name(func):
    def wrapper(*args, **kwargs):
        print(f"Starting of the function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending of the function: {func.__name__}")
        return result
    return wrapper

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        print(f'staring time of function execution:{time.time()}')
        starting_time = time.time()
        result = func(*args, **kwargs)
        print(f'ending time of function execution:{time.time()}')
        ending_time = time.time()
        print(f'Time required : {ending_time - starting_time}')
        return  result
    return wrapper

@log_execution_time
@log_func_name

def great():
    time.sleep(5)
great()