def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Starting of the function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending of the function: {func.__name__}")
        return result
    return wrapper

@decorator
def great(name):
    print(f"hi,{name}")

great("sachin")

