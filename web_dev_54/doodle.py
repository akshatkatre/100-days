## Decorators
import time


def delay_decorator(function):
    def wrapper_function():
        # Do something before
        time.sleep(2)
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print('hello')

@delay_decorator
def say_bye():
    print('bye')

say_hello()
say_bye()
# f = decorator_function(say_hello)
# f()
# f = decorator_function(say_bye)
# f()