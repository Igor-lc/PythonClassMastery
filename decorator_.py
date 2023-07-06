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
