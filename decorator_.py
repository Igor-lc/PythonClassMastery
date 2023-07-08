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
