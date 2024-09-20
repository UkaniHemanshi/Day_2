import logging

# logging.basicConfig(filename='basicConfig.log',level= logging.DEBUG, format="%(asctime)s -%(levelname)s -%(message)s")

logger = logging.getLogger('advancedconfig_logger')
handler = logging.FileHandler('advancedconfig_logger.log')
formatter = logging.Formatter('%(asctime)s - %(name)s-%(levelname)s -%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def log_execution(func):
    def wrapper(*args, **kwargs):
        logger.debug('debug message')
        print(f"Before function execute: {func.__name__} function has begin")
        result = func(*args, **kwargs)
        print(f"After function executes: {func.__name__} has ended")
        logger.debug('debug message')
        return result
    return wrapper

@log_execution
def S_func(name):
    print(f'hello world: {name}')
S_func("sachin")