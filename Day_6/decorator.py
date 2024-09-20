#Decorator function that takes the function to be decorated
def simple_logger(func):
    #wrapper function that adds logging behaviour
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs) #call the original function
        print(f"Finished {func.__name__}.")
        return result
    return wrapper

#using the decorator without arguments
@simple_logger
def greet(name):
    print(f"Hello, {name}!")
#calling the decorated function
greet("kmnnjjk")