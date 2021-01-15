def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f'You called {function.__name__} {args}')
        return function(args[0], args[1])
    return wrapper_function

@logging_decorator
def sum(a, b):
    return a + b

@logging_decorator
def substract(a, b):
    return a - b

print(sum(1,2))
print(substract(1,2))

