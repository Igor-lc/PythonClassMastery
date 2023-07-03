def second_outer(*a, **k):
    def outer(func):
        def inner(*args, **kwargs):
            print(*a, **k)
            return func(*args, **kwargs)
        return inner
    return outer

@second_outer("Реклама")
def div(a, b):
    return a / b


print(div(1, 2))
