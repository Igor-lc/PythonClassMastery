def second(func):
    print("second")
    def first(*args):
        print("first")
        return f"{func(*args)}, {args}"
    return first

@second
def div(a, b):
    return a * b

print(div(10, 5))
print(div(10, 5))
print(div(10, 5))