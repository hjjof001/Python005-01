class _map:

    def __init__(self, func, *iterables):
        self.func = func
        self.iters = [iter(iterable) for iterable in iterables]

    def __iter__(self):
        return self

    def __next__(self):
        value = self.func(*[next(it) for it in self.iters])
        return value


def square(x):
    return x * x


res = _map(square, [1, 2, 3, 4, 5, 6])
print(list(res))
