def add(*args):
    print(type(args), args[1])
    total: int = 0
    for n in args:
        print(n)
        total += n
    return total


print(f"total: {add(1,2,2,3,4,5,6)}")
