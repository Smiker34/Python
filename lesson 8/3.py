from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logs = {}
        for arg in args:
            logs[arg] = type(arg)
        for value in kwargs.values():
            logs[value] = type(value)
        print(func.__name__, logs)
        return func(*args), type(func(*args))
    return wrapper

@type_logger
def arithmetic(x,y,z):
    return (x + y) * z

print(arithmetic(4,3,5))