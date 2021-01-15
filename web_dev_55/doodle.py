class User:
    def __init__(self, name, is_logged_in):
        self.name = name
        self.is_logged_in = is_logged_in

def is_authenticated(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper_function

@is_authenticated
def print_user(u: User):
    print(f"The user name is {u.name}")


user1 = User('aks', True)
user2 = User('joe', False)
print_user(user1)
print_user(user2)