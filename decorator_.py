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
