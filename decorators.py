def third(*args2):
    print("third")
    def second(func):
        print("second")
        def first(*args):
            print("first")
            return f"{func(*args)}, {func(*args2)}"
        return first
    return second

@third(10, 10)
def div(a, b):
    return a + b
print(div(10, 5))
print(div(10, 5))
print(div(10, 5))


def register_call(func):
    def w(*args):
        w.c += 1
        print("reg_call =", w.c)
        return func(*args)
    w.c = 0
    return w

@register_call
def test(a, b):
    return a * b
print(test(1, 2))
print(test(2, 3))


def check(func):
    def odd_even(*args):
        for i, el in enumerate(args[1:], 1):
            if (args[i - 1] & 1) != (el & 1):
                return "odd_even"
        return('even', 'odd')[args[0] & 1]

    return odd_even

@check
def test(*args):
    pass
print(test(1, 1, 1, 1, 1))



import time
def time_(func):
    def inner(*args):
        start = time.time()
        result = func(*args)
        elapsed_time = time.time() - start
        print("Time taken:", elapsed_time)
        return result
    return inner

@time_
def div(a, b):
    return a / b
print(div(1, 1))


'''Repeat Execution
Create a decorator that repeats the execution of a function a specified number of times. The decorator should take the number of repetitions as an argument.'''

def repeat_execution(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
                print("Result:", result)
            return result
        return wrapper
    return decorator

@repeat_execution(3)
def multiply(a, b):
    return a * b

multiply(2, 5)
