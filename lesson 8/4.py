def val_checker(condition):
    def check(func):
        def wrapper(*args):
            for arg in args:
                if condition(arg) is False:
                    raise ValueError("Некорректное значение: %d" % (arg))
            return func(*args)
        return wrapper
    return check
@val_checker(lambda x: x > 0)
def cube(x):
    return x ** 3

print(cube(3))